from datetime import datetime

stake = {
    "id": 1,
    "amount_staked": 12000,
    "start_date": datetime(2023,1,17),
    "staked_days": 90,  # 90, 180, 365 -> default is 90
    "profits": 0.0,
    "available_funds": 0.0,
    "status": "PENDING",  # PENDING, ACTIVE, TERMINATED, MATURED, ONHOLD
    # {"request_amount_to_withdraw": 0.0, "amount_withdrawn": 0.0, "date_withdrawn": datetime.now(), "charges": 0.0, "taxes": 0.0, "deductions": 0.0, "currency": "UGX"},
    "withdraws": [],

    "profits":[ 
            {
                "interest_rate": 0.03,
                "current_profit": 3180.0,
                "expected_profit": 3180.0,
                "id": "caa207e2-df2c-41d2-a4ac-302f01037302",
                "balance": 15180.0
            }
    ]
}



from enum import Enum


class StakeStatus(Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    ONHOLD = "ONHOLD"
    MATURED = "MATURED"
    RESTAKED = "RESTAKED"
    FULLY_WITHDRAWN = "FULLY_WITHDRAWN"
    PARTIALLY_WITHDRAWN = "PARTIALLY_WITHDRAWN"
    FAILED = "FAILED"


def backdate_stake(stake, number_of_days=None):
    if stake.get("status") in [
        StakeStatus.REJECTED,
        StakeStatus.PENDING,
        StakeStatus.ONHOLD,
    ]:
        raise Exception("you are trying to back date a stake thats not active")

    interest_rate = 0.03
    days_staked = (datetime.now() - stake.get("start_date")).days
    daily_profit = (interest_rate * stake.get('amount_staked')) / 30

    current_profit = daily_profit * days_staked

    amount_available = stake.get("amount_staked") + current_profit


    if number_of_days is not None:
        current_profit = daily_profit * number_of_days

        amount_available = stake['profits'][0]['balance'] + current_profit

    stake['profits'][0]['current_profit'] = current_profit
    stake['profits'][0]['balance'] = amount_available

    return {
        "amount_staked": stake.get("amount_staked"),
        "daily_profit": daily_profit,
        "days_staked": days_staked,
        "current_profit": current_profit,
        "amount_available": amount_available,
    }


print(f"backdate after no days, {backdate_stake(stake)}")
print(f"backdate to 100 days, {backdate_stake(stake,100)}")
print(f"backdate to 120 days, {backdate_stake(stake,120)}")
print(f"backdate to 180 days, {backdate_stake(stake,180)}")

