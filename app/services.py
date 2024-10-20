class PowerPlantService:

    @classmethod
    def get_sorted_plants(cls, data):
        marginal_costs = []
        co2_costs = 0.3 # cost per MWh generated

        # calculate each powerplant costs
        for plant in data.powerplants:
            if plant.type == "gasfired":
                fuel_cost = data.fuels.gas
                marginal_cost = (fuel_cost / plant.efficiency) * co2_costs
            elif plant.type == "turbojet":
                fuel_cost = data.fuels.kerosine
                marginal_cost = (fuel_cost / plant.efficiency) * co2_costs
            elif plant.type == "windturbine":
                marginal_cost = 0

            marginal_costs.append(
                {"power_plant": plant.name, "marginal_cost": marginal_cost}
            )

        # sort plants based on marginal costs
        sorted_plants = sorted(marginal_costs, key=lambda x: x['marginal_cost'])
        return sorted_plants

    @classmethod
    def get_production_plant(cls, data, sorted_plants):
        load = data.load
        remaining_load = load
        production_plan = []

        for order_plant in sorted_plants:
            # search powerplant object
            plant_name = order_plant.get("power_plant")
            for plant in data.powerplants:
                if plant.name == plant_name:
                    power_plant = plant
            # reduce the turbine efficiency
            if power_plant.type == "windturbine":
                max_power = round(power_plant.pmax * (data.fuels.wind / 100), 2)
            else:
                max_power = power_plant.pmax
            if remaining_load > 0:
                # select max between pmin & remaining load
                capacity_power = max(power_plant.pmin, remaining_load)
                # select min between allowed_power & max_power
                power_assigned = min(capacity_power, max_power)
                production_plan.append({"name": power_plant.name, "p": power_assigned})
                remaining_load -= power_assigned
            else:
                # no power when remaining load is reached
                production_plan.append({"name": power_plant.name, "p": 0})
        return production_plan
