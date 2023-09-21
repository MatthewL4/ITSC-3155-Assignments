
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient) < quantity:
                return False
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):

