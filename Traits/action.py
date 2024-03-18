from Traits.trait import Trait

class Action(Trait):

    def __init__(self, name, effectKey, targeting="Standard", maxCharges=-1, recharge="Turn", rechargePercent=1, aiPrio=0, range = 1, length = 1, width = 1) -> None:
        super().__init__(name, "Active", effectKey, targeting, maxCharges, recharge, rechargePercent, aiPrio, range, length, width)

class enemAction(Action):

    def __init__(self, effectKey, targeting="Standard", maxCharges=-1, recharge="Turn", rechargePercent=1, aiPrio=0, range=1, length=1, width=1) -> None:
        super().__init__("No Name", effectKey, targeting, maxCharges, recharge, rechargePercent, aiPrio, range, length, width)
