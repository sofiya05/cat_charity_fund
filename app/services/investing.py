from datetime import datetime

from app.models.base import BaseCharityDonationModel


def investing_process(
    target: BaseCharityDonationModel,
    sources: list[BaseCharityDonationModel],
) -> list[BaseCharityDonationModel]:

    modified_sources = []

    for source in sources:
        transfer_amount = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount,
        )
        if transfer_amount == 0:
            break

        target.invested_amount += transfer_amount
        source.invested_amount += transfer_amount

        if target.full_amount == target.invested_amount:
            target.fully_invested = True
            target.close_date = datetime.now()

        if source.full_amount == source.invested_amount:
            source.fully_invested = True
            source.close_date = datetime.now()

        modified_sources.append(source)

        if target.fully_invested:
            break

    return modified_sources
