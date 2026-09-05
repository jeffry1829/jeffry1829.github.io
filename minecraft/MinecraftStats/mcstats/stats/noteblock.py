from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'noteblock',
        {
            'title': '音樂家',
            'desc': '音階箱調音次數',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:tune_noteblock']),
            mcstats.StatReader(['minecraft:custom','minecraft:play_noteblock'])])
    ))
