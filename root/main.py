import csv
rows_print =[
            ["asteroid_id", "ore_units" , "crystal_units", "gas_units", "cargo_value", "total"],
        ]
with open("input_asteroid_data.csv", "r",) as file:
    the_input = csv.DictReader(file)
    for row in the_input:
        print(row["asteroid_id"],row["ore_units"], row["crystal_units"], row["gas_units"])
        cargo_value_ore = (int(row["ore_units"]) * 2)
        cargo_value_gas = (int(row["gas_units"]) * 3)
        cargo_value_crystal = (int(row["crystal_units"]) * 5)
        cargo_value = (cargo_value_ore + cargo_value_gas + cargo_value_crystal)
        print(cargo_value)
        total = int(row["ore_units"]) + int(row["gas_units"]) + int(row["crystal_units"])
        print(total)
        c_units = int(row["crystal_units"])
        g_units = int(row["gas_units"])
        o_units = int(row["ore_units"])
        id = row["asteroid_id"]
        rows_print.append([ id, o_units, c_units, g_units, cargo_value, total ])

        with open("output_asteroid_data.csv", "w", newline="" ) as file:
            writer = csv.writer(file)
            writer.writerows(rows_print)
