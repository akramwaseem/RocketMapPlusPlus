# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/badge_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/badge_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!pogoprotos/enums/badge_type.proto\x12\x10pogoprotos.enums*\x84\x16\n\tBadgeType\x12\x0f\n\x0b\x42\x41\x44GE_UNSET\x10\x00\x12\x13\n\x0f\x42\x41\x44GE_TRAVEL_KM\x10\x01\x12\x19\n\x15\x42\x41\x44GE_POKEDEX_ENTRIES\x10\x02\x12\x17\n\x13\x42\x41\x44GE_CAPTURE_TOTAL\x10\x03\x12\x17\n\x13\x42\x41\x44GE_DEFEATED_FORT\x10\x04\x12\x17\n\x13\x42\x41\x44GE_EVOLVED_TOTAL\x10\x05\x12\x17\n\x13\x42\x41\x44GE_HATCHED_TOTAL\x10\x06\x12\x1b\n\x17\x42\x41\x44GE_ENCOUNTERED_TOTAL\x10\x07\x12\x1b\n\x17\x42\x41\x44GE_POKESTOPS_VISITED\x10\x08\x12\x1a\n\x16\x42\x41\x44GE_UNIQUE_POKESTOPS\x10\t\x12\x19\n\x15\x42\x41\x44GE_POKEBALL_THROWN\x10\n\x12\x16\n\x12\x42\x41\x44GE_BIG_MAGIKARP\x10\x0b\x12\x18\n\x14\x42\x41\x44GE_DEPLOYED_TOTAL\x10\x0c\x12\x1b\n\x17\x42\x41\x44GE_BATTLE_ATTACK_WON\x10\r\x12\x1d\n\x19\x42\x41\x44GE_BATTLE_TRAINING_WON\x10\x0e\x12\x1b\n\x17\x42\x41\x44GE_BATTLE_DEFEND_WON\x10\x0f\x12\x19\n\x15\x42\x41\x44GE_PRESTIGE_RAISED\x10\x10\x12\x1a\n\x16\x42\x41\x44GE_PRESTIGE_DROPPED\x10\x11\x12\x15\n\x11\x42\x41\x44GE_TYPE_NORMAL\x10\x12\x12\x17\n\x13\x42\x41\x44GE_TYPE_FIGHTING\x10\x13\x12\x15\n\x11\x42\x41\x44GE_TYPE_FLYING\x10\x14\x12\x15\n\x11\x42\x41\x44GE_TYPE_POISON\x10\x15\x12\x15\n\x11\x42\x41\x44GE_TYPE_GROUND\x10\x16\x12\x13\n\x0f\x42\x41\x44GE_TYPE_ROCK\x10\x17\x12\x12\n\x0e\x42\x41\x44GE_TYPE_BUG\x10\x18\x12\x14\n\x10\x42\x41\x44GE_TYPE_GHOST\x10\x19\x12\x14\n\x10\x42\x41\x44GE_TYPE_STEEL\x10\x1a\x12\x13\n\x0f\x42\x41\x44GE_TYPE_FIRE\x10\x1b\x12\x14\n\x10\x42\x41\x44GE_TYPE_WATER\x10\x1c\x12\x14\n\x10\x42\x41\x44GE_TYPE_GRASS\x10\x1d\x12\x17\n\x13\x42\x41\x44GE_TYPE_ELECTRIC\x10\x1e\x12\x16\n\x12\x42\x41\x44GE_TYPE_PSYCHIC\x10\x1f\x12\x12\n\x0e\x42\x41\x44GE_TYPE_ICE\x10 \x12\x15\n\x11\x42\x41\x44GE_TYPE_DRAGON\x10!\x12\x13\n\x0f\x42\x41\x44GE_TYPE_DARK\x10\"\x12\x14\n\x10\x42\x41\x44GE_TYPE_FAIRY\x10#\x12\x17\n\x13\x42\x41\x44GE_SMALL_RATTATA\x10$\x12\x11\n\rBADGE_PIKACHU\x10%\x12\x0f\n\x0b\x42\x41\x44GE_UNOWN\x10&\x12\x1e\n\x1a\x42\x41\x44GE_POKEDEX_ENTRIES_GEN2\x10\'\x12\x19\n\x15\x42\x41\x44GE_RAID_BATTLE_WON\x10(\x12\x1e\n\x1a\x42\x41\x44GE_LEGENDARY_BATTLE_WON\x10)\x12\x15\n\x11\x42\x41\x44GE_BERRIES_FED\x10*\x12\x18\n\x14\x42\x41\x44GE_HOURS_DEFENDED\x10+\x12\x16\n\x12\x42\x41\x44GE_PLACE_HOLDER\x10,\x12\x1e\n\x1a\x42\x41\x44GE_POKEDEX_ENTRIES_GEN3\x10-\x12\x1a\n\x16\x42\x41\x44GE_CHALLENGE_QUESTS\x10.\x12\x17\n\x13\x42\x41\x44GE_MEW_ENCOUNTER\x10/\x12\x1b\n\x17\x42\x41\x44GE_MAX_LEVEL_FRIENDS\x10\x30\x12\x11\n\rBADGE_TRADING\x10\x31\x12\x1a\n\x16\x42\x41\x44GE_TRADING_DISTANCE\x10\x32\x12\x1e\n\x1a\x42\x41\x44GE_POKEDEX_ENTRIES_GEN4\x10\x33\x12\x16\n\x12\x42\x41\x44GE_GREAT_LEAGUE\x10\x34\x12\x16\n\x12\x42\x41\x44GE_ULTRA_LEAGUE\x10\x35\x12\x17\n\x13\x42\x41\x44GE_MASTER_LEAGUE\x10\x36\x12\x14\n\x0f\x42\x41\x44GE_EVENT_MIN\x10\xd0\x0f\x12!\n\x1c\x42\x41\x44GE_CHICAGO_FEST_JULY_2017\x10\xd1\x0f\x12)\n$BADGE_PIKACHU_OUTBREAK_YOKOHAMA_2017\x10\xd2\x0f\x12\"\n\x1d\x42\x41\x44GE_SAFARI_ZONE_EUROPE_2017\x10\xd3\x0f\x12(\n#BADGE_SAFARI_ZONE_EUROPE_2017_10_07\x10\xd4\x0f\x12(\n#BADGE_SAFARI_ZONE_EUROPE_2017_10_14\x10\xd5\x0f\x12+\n&BADGE_CHICAGO_FEST_JULY_2018_SAT_NORTH\x10\xd6\x0f\x12+\n&BADGE_CHICAGO_FEST_JULY_2018_SAT_SOUTH\x10\xd7\x0f\x12+\n&BADGE_CHICAGO_FEST_JULY_2018_SUN_NORTH\x10\xd8\x0f\x12+\n&BADGE_CHICAGO_FEST_JULY_2018_SUN_SOUTH\x10\xd9\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_0\x10\xda\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_1\x10\xdb\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_2\x10\xdc\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_3\x10\xdd\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_4\x10\xde\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_5\x10\xdf\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_6\x10\xe0\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_7\x10\xe1\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_8\x10\xe2\x0f\x12#\n\x1e\x42\x41\x44GE_APAC_PARTNER_JULY_2018_9\x10\xe3\x0f\x12&\n!BADGE_YOKOSUKA_29_AUG_2018_MIKASA\x10\xe4\x0f\x12%\n BADGE_YOKOSUKA_29_AUG_2018_VERNY\x10\xe5\x0f\x12(\n#BADGE_YOKOSUKA_29_AUG_2018_KURIHAMA\x10\xe6\x0f\x12&\n!BADGE_YOKOSUKA_30_AUG_2018_MIKASA\x10\xe7\x0f\x12%\n BADGE_YOKOSUKA_30_AUG_2018_VERNY\x10\xe8\x0f\x12(\n#BADGE_YOKOSUKA_30_AUG_2018_KURIHAMA\x10\xe9\x0f\x12&\n!BADGE_YOKOSUKA_31_AUG_2018_MIKASA\x10\xea\x0f\x12%\n BADGE_YOKOSUKA_31_AUG_2018_VERNY\x10\xeb\x0f\x12(\n#BADGE_YOKOSUKA_31_AUG_2018_KURIHAMA\x10\xec\x0f\x12%\n BADGE_YOKOSUKA_1_SEP_2018_MIKASA\x10\xed\x0f\x12$\n\x1f\x42\x41\x44GE_YOKOSUKA_1_SEP_2018_VERNY\x10\xee\x0f\x12\'\n\"BADGE_YOKOSUKA_1_SEP_2018_KURIHAMA\x10\xef\x0f\x12%\n BADGE_YOKOSUKA_2_SEP_2018_MIKASA\x10\xf0\x0f\x12$\n\x1f\x42\x41\x44GE_YOKOSUKA_2_SEP_2018_VERNY\x10\xf1\x0f\x12\'\n\"BADGE_YOKOSUKA_2_SEP_2018_KURIHAMA\x10\xf2\x0f\x12\x17\n\x12\x42\x41\x44GE_TOP_BANANA_1\x10\xf3\x0f\x12\x17\n\x12\x42\x41\x44GE_TOP_BANANA_2\x10\xf4\x0f\x12\x17\n\x12\x42\x41\x44GE_TOP_BANANA_3\x10\xf5\x0f\x62\x06proto3')
)

_BADGETYPE = _descriptor.EnumDescriptor(
  name='BadgeType',
  full_name='pogoprotos.enums.BadgeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TRAVEL_KM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CAPTURE_TOTAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_DEFEATED_FORT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_EVOLVED_TOTAL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_HATCHED_TOTAL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_ENCOUNTERED_TOTAL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKESTOPS_VISITED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNIQUE_POKESTOPS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEBALL_THROWN', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BIG_MAGIKARP', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_DEPLOYED_TOTAL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_ATTACK_WON', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_TRAINING_WON', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_DEFEND_WON', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PRESTIGE_RAISED', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PRESTIGE_DROPPED', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_NORMAL', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FIGHTING', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FLYING', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_POISON', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GROUND', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ROCK', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_BUG', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GHOST', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_STEEL', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FIRE', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_WATER', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GRASS', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ELECTRIC', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_PSYCHIC', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ICE', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_DRAGON', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_DARK', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FAIRY', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_SMALL_RATTATA', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PIKACHU', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNOWN', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES_GEN2', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_RAID_BATTLE_WON', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_LEGENDARY_BATTLE_WON', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BERRIES_FED', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_HOURS_DEFENDED', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PLACE_HOLDER', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES_GEN3', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHALLENGE_QUESTS', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_MEW_ENCOUNTER', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_MAX_LEVEL_FRIENDS', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TRADING', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TRADING_DISTANCE', index=50, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES_GEN4', index=51, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_GREAT_LEAGUE', index=52, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_ULTRA_LEAGUE', index=53, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_MASTER_LEAGUE', index=54, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_EVENT_MIN', index=55, number=2000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHICAGO_FEST_JULY_2017', index=56, number=2001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PIKACHU_OUTBREAK_YOKOHAMA_2017', index=57, number=2002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_SAFARI_ZONE_EUROPE_2017', index=58, number=2003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_SAFARI_ZONE_EUROPE_2017_10_07', index=59, number=2004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_SAFARI_ZONE_EUROPE_2017_10_14', index=60, number=2005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHICAGO_FEST_JULY_2018_SAT_NORTH', index=61, number=2006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHICAGO_FEST_JULY_2018_SAT_SOUTH', index=62, number=2007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHICAGO_FEST_JULY_2018_SUN_NORTH', index=63, number=2008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CHICAGO_FEST_JULY_2018_SUN_SOUTH', index=64, number=2009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_0', index=65, number=2010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_1', index=66, number=2011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_2', index=67, number=2012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_3', index=68, number=2013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_4', index=69, number=2014,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_5', index=70, number=2015,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_6', index=71, number=2016,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_7', index=72, number=2017,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_8', index=73, number=2018,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_APAC_PARTNER_JULY_2018_9', index=74, number=2019,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_29_AUG_2018_MIKASA', index=75, number=2020,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_29_AUG_2018_VERNY', index=76, number=2021,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_29_AUG_2018_KURIHAMA', index=77, number=2022,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_30_AUG_2018_MIKASA', index=78, number=2023,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_30_AUG_2018_VERNY', index=79, number=2024,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_30_AUG_2018_KURIHAMA', index=80, number=2025,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_31_AUG_2018_MIKASA', index=81, number=2026,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_31_AUG_2018_VERNY', index=82, number=2027,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_31_AUG_2018_KURIHAMA', index=83, number=2028,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_1_SEP_2018_MIKASA', index=84, number=2029,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_1_SEP_2018_VERNY', index=85, number=2030,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_1_SEP_2018_KURIHAMA', index=86, number=2031,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_2_SEP_2018_MIKASA', index=87, number=2032,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_2_SEP_2018_VERNY', index=88, number=2033,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_YOKOSUKA_2_SEP_2018_KURIHAMA', index=89, number=2034,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TOP_BANANA_1', index=90, number=2035,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TOP_BANANA_2', index=91, number=2036,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TOP_BANANA_3', index=92, number=2037,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=56,
  serialized_end=2876,
)
_sym_db.RegisterEnumDescriptor(_BADGETYPE)

BadgeType = enum_type_wrapper.EnumTypeWrapper(_BADGETYPE)
BADGE_UNSET = 0
BADGE_TRAVEL_KM = 1
BADGE_POKEDEX_ENTRIES = 2
BADGE_CAPTURE_TOTAL = 3
BADGE_DEFEATED_FORT = 4
BADGE_EVOLVED_TOTAL = 5
BADGE_HATCHED_TOTAL = 6
BADGE_ENCOUNTERED_TOTAL = 7
BADGE_POKESTOPS_VISITED = 8
BADGE_UNIQUE_POKESTOPS = 9
BADGE_POKEBALL_THROWN = 10
BADGE_BIG_MAGIKARP = 11
BADGE_DEPLOYED_TOTAL = 12
BADGE_BATTLE_ATTACK_WON = 13
BADGE_BATTLE_TRAINING_WON = 14
BADGE_BATTLE_DEFEND_WON = 15
BADGE_PRESTIGE_RAISED = 16
BADGE_PRESTIGE_DROPPED = 17
BADGE_TYPE_NORMAL = 18
BADGE_TYPE_FIGHTING = 19
BADGE_TYPE_FLYING = 20
BADGE_TYPE_POISON = 21
BADGE_TYPE_GROUND = 22
BADGE_TYPE_ROCK = 23
BADGE_TYPE_BUG = 24
BADGE_TYPE_GHOST = 25
BADGE_TYPE_STEEL = 26
BADGE_TYPE_FIRE = 27
BADGE_TYPE_WATER = 28
BADGE_TYPE_GRASS = 29
BADGE_TYPE_ELECTRIC = 30
BADGE_TYPE_PSYCHIC = 31
BADGE_TYPE_ICE = 32
BADGE_TYPE_DRAGON = 33
BADGE_TYPE_DARK = 34
BADGE_TYPE_FAIRY = 35
BADGE_SMALL_RATTATA = 36
BADGE_PIKACHU = 37
BADGE_UNOWN = 38
BADGE_POKEDEX_ENTRIES_GEN2 = 39
BADGE_RAID_BATTLE_WON = 40
BADGE_LEGENDARY_BATTLE_WON = 41
BADGE_BERRIES_FED = 42
BADGE_HOURS_DEFENDED = 43
BADGE_PLACE_HOLDER = 44
BADGE_POKEDEX_ENTRIES_GEN3 = 45
BADGE_CHALLENGE_QUESTS = 46
BADGE_MEW_ENCOUNTER = 47
BADGE_MAX_LEVEL_FRIENDS = 48
BADGE_TRADING = 49
BADGE_TRADING_DISTANCE = 50
BADGE_POKEDEX_ENTRIES_GEN4 = 51
BADGE_GREAT_LEAGUE = 52
BADGE_ULTRA_LEAGUE = 53
BADGE_MASTER_LEAGUE = 54
BADGE_EVENT_MIN = 2000
BADGE_CHICAGO_FEST_JULY_2017 = 2001
BADGE_PIKACHU_OUTBREAK_YOKOHAMA_2017 = 2002
BADGE_SAFARI_ZONE_EUROPE_2017 = 2003
BADGE_SAFARI_ZONE_EUROPE_2017_10_07 = 2004
BADGE_SAFARI_ZONE_EUROPE_2017_10_14 = 2005
BADGE_CHICAGO_FEST_JULY_2018_SAT_NORTH = 2006
BADGE_CHICAGO_FEST_JULY_2018_SAT_SOUTH = 2007
BADGE_CHICAGO_FEST_JULY_2018_SUN_NORTH = 2008
BADGE_CHICAGO_FEST_JULY_2018_SUN_SOUTH = 2009
BADGE_APAC_PARTNER_JULY_2018_0 = 2010
BADGE_APAC_PARTNER_JULY_2018_1 = 2011
BADGE_APAC_PARTNER_JULY_2018_2 = 2012
BADGE_APAC_PARTNER_JULY_2018_3 = 2013
BADGE_APAC_PARTNER_JULY_2018_4 = 2014
BADGE_APAC_PARTNER_JULY_2018_5 = 2015
BADGE_APAC_PARTNER_JULY_2018_6 = 2016
BADGE_APAC_PARTNER_JULY_2018_7 = 2017
BADGE_APAC_PARTNER_JULY_2018_8 = 2018
BADGE_APAC_PARTNER_JULY_2018_9 = 2019
BADGE_YOKOSUKA_29_AUG_2018_MIKASA = 2020
BADGE_YOKOSUKA_29_AUG_2018_VERNY = 2021
BADGE_YOKOSUKA_29_AUG_2018_KURIHAMA = 2022
BADGE_YOKOSUKA_30_AUG_2018_MIKASA = 2023
BADGE_YOKOSUKA_30_AUG_2018_VERNY = 2024
BADGE_YOKOSUKA_30_AUG_2018_KURIHAMA = 2025
BADGE_YOKOSUKA_31_AUG_2018_MIKASA = 2026
BADGE_YOKOSUKA_31_AUG_2018_VERNY = 2027
BADGE_YOKOSUKA_31_AUG_2018_KURIHAMA = 2028
BADGE_YOKOSUKA_1_SEP_2018_MIKASA = 2029
BADGE_YOKOSUKA_1_SEP_2018_VERNY = 2030
BADGE_YOKOSUKA_1_SEP_2018_KURIHAMA = 2031
BADGE_YOKOSUKA_2_SEP_2018_MIKASA = 2032
BADGE_YOKOSUKA_2_SEP_2018_VERNY = 2033
BADGE_YOKOSUKA_2_SEP_2018_KURIHAMA = 2034
BADGE_TOP_BANANA_1 = 2035
BADGE_TOP_BANANA_2 = 2036
BADGE_TOP_BANANA_3 = 2037


DESCRIPTOR.enum_types_by_name['BadgeType'] = _BADGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
