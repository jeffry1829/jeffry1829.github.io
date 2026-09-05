from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_dealt',
        {
            'title': '狂戰士!',
            'desc': '造成的傷害值',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_dealt'])
    ))
