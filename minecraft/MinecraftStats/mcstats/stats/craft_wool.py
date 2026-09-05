from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_wool',
        {
            'title': '紡織師',
            'desc': '羊毛/地毯的製造/染色數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_wool',
                'minecraft:.+_carpet'
            ])
    ))
