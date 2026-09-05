from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'trigger_raid',
        {
            'title': '我有不好的預感',
            'desc': '觸發突襲次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:raid_trigger']),
        1912 # raids added in 18w47a
    ))
