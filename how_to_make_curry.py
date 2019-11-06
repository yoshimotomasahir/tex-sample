def how_to_make_curry(materials, something_spicy, rice, water):
    # Curry part
    materials = cut(materials)
    pot = mix(materials, water)
    with open("Gas stove") as fire:
        pot = fire.to(pot)
    pot.add(something_spicy)

    # Rice part
    rice = mix(rice, water)
    with open("Rice cooker") as heat:
        rice = heat.to(rice)

    dish = mix(pot.inside(), rice)
    print("I'm happy!")
