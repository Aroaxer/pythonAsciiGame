from Traits.trait import Trait

class Action(Trait):

    def __init__(self, effectKey, targeting="Standard", maxCharges=-1, recharge="Turn", rechargePercent=1, aiPrio=0, range = 1, length = 0, width = 0) -> None:
        super().__init__("Active", effectKey, targeting, maxCharges, recharge, rechargePercent, aiPrio, range, length, width)