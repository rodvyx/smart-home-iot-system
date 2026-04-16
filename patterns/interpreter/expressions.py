from patterns.interpreter.expression import Expression


class EnergyGreaterThan(Expression):
    def __init__(self, threshold):
        self.threshold = threshold

    def interpret(self, context):
        return context.energy_value > self.threshold


class TurnOffCommand(Expression):
    def interpret(self, context):
        return "Turning off devices due to high energy usage"


# ✅ THIS WAS MISSING — ADD IT HERE
class IfThenExpression(Expression):
    def __init__(self, condition: Expression, action: Expression):
        self.condition = condition
        self.action = action

    def interpret(self, context):
        if self.condition.interpret(context):
            return self.action.interpret(context)
        return "Condition not met"