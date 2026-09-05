from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_armor',
        {
            'title': '盔甲匠',
            'desc': '造過的盔甲數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_helmet',
                'minecraft:.+_leggings',
                'minecraft:.+_boots',
                'minecraft:.+_chestplate',
                'minecraft:shield',
            ])
    ))
