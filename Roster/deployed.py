"""Use a roster file to find who is deployed in regions.

Based on https://github.com/HN67/nsapi/blob/master/roster/deployed.py
but adapted to work with sans."""

import typing as t

import sans
from sans.api import Api


def clean_format(nation: str) -> str:
    """Converts a nation name to API form."""
    return nation.replace(" ", "_").lower()


async def endorsements(nation: str) -> t.Iterable[str]:
    """Query NS API for the endorsements of a nation."""
    Api.agent = "10000 Islands Discord Bot contact Kortexia"
    request = Api(
        "endorsements",
        nation=nation,
    )
    try:
        root = await request
    except sans.errors.HTTPException:
        return []
    else:
        return root.ENDORSEMENTS.text.split(",")


async def deployed(
    lead: str,
    roster: t.Mapping[str, t.Iterable[str]],
) -> t.Tuple[t.Collection[t.Tuple[str, str]], t.Collection[str]]:
    """Determine who are deployed and endorsing the lead.

    Returns a tuple of those known to be deployed on and including the lead,
    and a collection of puppets whose owners are unknown.
    """
    # Invert roster into puppet -> main form
    owners = {
        clean_format(switcher): main
        for main, switchers in roster.items()
        for switcher in switchers
    }
    # Also include main nations
    owners.update({clean_format(main): main for main in roster.keys()})
    # Obtain endorsement list of lead
    endos = map(clean_format, await endorsements(lead))
    # We also want to include the lead in those deployed
    deployed_puppets = list(endos) + [clean_format(lead)]
    # Return owners who have a nation endoing lead
    return (
        [(owners[nation], nation) for nation in deployed_puppets if nation in owners],
        [puppet for puppet in deployed_puppets if puppet not in owners],
    )


class Deployments(t.NamedTuple):
    """Info on the deployments on a lead."""

    known: t.Collection[str]
    puppets: t.Collection[str]
    unknown: t.Collection[str]


async def deployed_lists(
    lead: str, roster: t.Mapping[str, t.Iterable[str]]
) -> Deployments:
    """Calculate deployed, deployed puppets, and unknown puppets on a lead."""
    endorsers, unknown = await deployed(lead=lead, roster=roster)
    # yeah this works. zip(*iterable) is its own inverse
    # kinda mind bending but it checks out
    # we need to strictly evaluate the zip using list so that we can tell if its empty
    seperated_endorsers = list(zip(*sorted(endorsers)))
    # If there are no endorsers, [] is inverted to [] which we can't split
    if seperated_endorsers:
        endorser_names, endorser_puppets = seperated_endorsers
    else:
        endorser_names, endorser_puppets = tuple(), tuple()
    return Deployments(endorser_names, endorser_puppets, unknown)
