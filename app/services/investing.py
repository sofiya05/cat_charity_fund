from datetime import datetime

from app.models.base import BaseCharityDonationModel


def investing_process(
    target: BaseCharityDonationModel,
    sources: list[BaseCharityDonationModel],
) -> BaseCharityDonationModel:

    for source in sources:

        free_amount_target = target.full_amount - int(target.invested_amount)
        free_amount_source = source.full_amount - source.invested_amount
        transfer_amount = min(free_amount_target, free_amount_source)

        for obj, free_amount in [
            (target, free_amount_target),
            (source, free_amount_source),
        ]:
            obj.invested_amount += transfer_amount
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()

    return target
