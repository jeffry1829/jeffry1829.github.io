from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_paper',
        {
            'title': '紙男孩',
            'desc': '製造紙的數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:paper'])
    ))
