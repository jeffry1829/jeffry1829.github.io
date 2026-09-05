from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sponge',
        {
            'title': '海綿寶寶',
            'desc': '製造的海綿數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:sponge'])
    ))
