from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'pot_flower',
        {
            'title': '花店',
            'desc': '種花(盆栽)數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pot_flower'])
    ))
