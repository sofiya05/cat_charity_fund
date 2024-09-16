from datetime import datetime

from app.models.base import BaseCharityDonationModel


def investing_process(
    target: BaseCharityDonationModel,
    sources: list[BaseCharityDonationModel],
) -> BaseCharityDonationModel:

    for source in sources:
        transfer_amount = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount,
        )
        if transfer_amount == 0:
            break

        for obj in [target, source]:
            obj.invested_amount += transfer_amount
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

    return target, sources
