import lightbulb
import hikari
import flare
from pymongo import MongoClient
plugin = lightbulb.Plugin('', '')

bo = None
client = MongoClient("mongodb+srv://brncray:Bobrien@bot.lvf7vud.mongodb.net/?retryWrites=true&w=majority")

penal_codes_cod = [
    "(1)01", "(1)02", "(1)03", "(1)04", "(1)05", "(1)06", "(1)07", "(1)08", "(1)09", "(1)10",
    "(1)11", "(1)12", "(1)13", "(1)14", "(1)15", "(1)16", "(1)17", "(1)18", "(1)19", "(1)20",
    "(1)21", "(2)01", "(2)02", "(2)03", "(2)04", "(2)05", "(2)06", "(2)07", "(2)08", "(2)09",
    "(2)10", "(2)11", "(2)12", "(2)13", "(2)14", "(2)15", "(2)16", "(2)17", "(2)18", "(2)19",
    "(2)20", "(2)21", "(2)22", "(2)23", "(2)24", "(2)25", "(2)26", "(2)27", "(3)01", "(3)02",
    "(3)03", "(3)04", "(3)05", "(3)06", "(3)07", "(3)08", "(3)09", "(3)10", "(3)11", "(3)12",
    "(3)13", "(3)14", "(3)15", "(3)16", "(3)17", "(4)01", "(4)02", "(4)03", "(4)04", "(4)05",
    "(4)06", "(4)07", "(5)01", "(5)02", "(5)03", "(5)04", "(5)05", "(5)06", "(5)07", "(5)08",
    "(5)09", "(5)10", "(5)11", "(5)12", "(5)13", "(5)14", "(6)01", "(6)02", "(6)03", "(6)04",
    "(6)05", "(6)06", "(6)07", "(6)08", "(6)09", "(6)10", "(6)11", "(6)12", "(6)13", "(6)14",
    "(6)15", "(6)16", "(6)17", "(6)18", "(6)19", "(6)20", "(6)21", "(6)22", "(6)23", "(6)24",
    "(6)25", "(6)26", "(6)27", "(6)28", "(6)29", "(6)30", "(6)31", "(6)32", "(6)33", "(6)34",
    "(6)35", "(6)36", "(6)37", "(6)38", "(6)39", "(6)40", "(6)41", "(6)42", "(6)43", "(6)44",
    "(6)45", "(6)46", "(6)47", "(6)48", "(6)49", "(6)50", "(6)51", "(6)52", "(6)53", "(6)54",
    "(7)01", "(7)02", "(7)03", "(7)04", "(7)05", "(7)06", "(7)07", "(7)08", "(7)09", "(7)10",
    "(7)11"
]


penal_codes_ref = [
  "(1)01 Intimidation (Major)",
  "(1)02 Intimidation (Minor)",
  "(1)03 Assault",
  "(1)04 Assault on LEO / Gov. Worker",
  "(1)05 Aggravated Assault",
  "(1)06 Battery",
  "(1)07 Aggravated Battery",
  "(1)08 Attempted Murder",
  "(1)09 Attempted Murder on LEO / Gov. Worker; 1st Degree",
  "(1)10 Attempted Murder; 2nd Degree",
  "(1)11 Voluntary Manslaughter",
  "(1)12 Criminally Negligent Homicide",
  "(1)13 Murder; 1st Degree",
  "(1)14 Murder; 2nd Degree",
  "(1)15 False Imprisonment",
  "(1)16 Aggravated Kidnapping",
  "(1)17 Simple Kidnapping",
  "(1)18 Robbery; 1st Degree",
  "(1)19 Robbery; 2nd Degree",
  "(1)20 Human Trafficking",
  "(1)21 Criminal Threats",
  "(2)01 Arson; 1st Degree",
  "(2)02 Arson; 2nd Degree",
  "(2)03 Reckless Burning; Felony",
  "(2)04 Reckless Burning; Misdemeanor",
  "(2)05 Trespassing",
  "(2)06 Trespassing within a Restricted Facility",
  "(2)07 Aggravated Trespassing",
  "(2)08 Burglary; 1st Degree",
  "(2)09 Burglary; 2nd Degree",
  "(2)10 Possession of Burglary Tools",
  "(2)11 Petty Theft",
  "(2)12 Theft",
  "(2)13 Grand Theft",
  "(2)14 Grand Theft Auto",
  "(2)15 Grand Theft of a Firearm",
  "(2)16 Receiving/Possession of Stolen Property",
  "(2)17 Extortion",
  "(2)18 Forgery",
  "(2)19 Fraud",
  "(2)20 Vandalism",
  "(2)21 Manufacturing Forged Documents",
  "(2)22 Manufacturing Forged Gov. Documents",
  "(2)23 Failure to Pay Fine",
  "(2)24 Destruction of Civilian/Private Property; 1st Degree",
  "(2)25 Destruction of Civilian/Private Property; 2nd Degree",
  "(2)26 Destruction of Civilian/Private Property; 3rd Degree",
  "(2)27 Destruction of Government Property",
  "(3)01 Bribery",
  "(3)02 Witness Tampering",
  "(3)03 False Information; 1st Degree",
  "(3)04 False Information; 2nd Degree",
  "(3)05 Filing a False Complaint",
  "(3)06 Impersonating a Government Official; Implied",
  "(3)07 Impersonating a Government Official; Deceiving",
  "(3)08 Impersonating a Government Official; Fraud",
  "(3)09 Failure to Identify to a Peace Officer",
  "(3)10 Obstruction of Justice",
  "(3)11 Resisting a Peace Officer; without Violence",
  "(3)12 Resisting a Peace Officer; with Violence",
  "(3)13 Escape from Custody",
  "(3)14 Tampering with Evidence",
  "(3)15 Conveyance within a Government Facility",
  "(3)16 Violation of Parole or Probation",
  "(3)17 Corruption from Public Duty",
  "(4)01 Disturbing the Peace",
  "(4)02 Incitement to Riot or Cause Violence",
  "(4)03 Street Racing",
  "(4)04 Refusal to Remove Facial Obstruction",
  "(4)05 Facial Obstruction whilst Committing a Crime",
  "(4)06 Disorderly Conduct",
  "(4)07 Interference with Government Operations",
  "(5)01 Possession of a Controlled Substance",
  "(5)02 Possession of a Controlled Substance with Intent to Sell",
  "(5)03 Possession of Drug Paraphernalia",
  "(5)04 Maintaining a Place for the Purpose of Distribution",
  "(5)05 Manufacture or Sale of a Controlled Substance",
  "(5)06 Possession of an Open Container",
  "(5)07 Public Intoxication",
  "(5)08 Animal Cruelty; Animal Abuse",
  "(5)09 Wanton Endangerment",
  "(5)10 Minor Alcohol Violation",
  "(5)11 Restricted Possession of a Firearm",
  "(5)12 Brandishing of a Firearm",
  "(5)13 Negligent Discharge of a Firearm",
  "(5)14 Drive-by Shooting; Shooting from a Vehicle",
  "(6)01 Driving with a Suspended/No License",
  "(6)02 Evading a Peace Officer",
  "(6)03 Reckless Evasion of a Peace Officer",
  "(6)04 Excessive Noise Violation",
  "(6)05 Hit & Run",
  "(6)06 Reckless Operation of Vehicle",
  "(6)07 Reckless Operation of Vehicle Causing Bodily Harm",
  "(6)08 3rd degree Speeding Violation",
  "(6)09 2nd Degree Speeding Violation",
  "(6)10 1st Degree Speeding Violation",
  "(6)11 Excessive Speeding Violation",
  "(6)12 Use of Nitrous Oxide",
  "(6)13 Failure to Stop",
  "(6)14 Lane Violation",
  "(6)15 Ignoring Traffic Signs",
  "(6)16 Disregard for Road Work",
  "(6)17 Failure to follow flow of traffic",
  "(6)18 Failure to Yield at an Intersection",
  "(6)19 Failure to Yield to a Pedestrian",
  "(6)20 Failure to Yield to Emergency Vehicles",
  "(6)21 Parking Violation",
  "(6)22 Impeding Traffic",
  "(6)23 Driving Under the Influence; Over Legal Limit",
  "(6)24 Driving Under the Influence; Drugs",
  "(6)25 Failure to Register a Vehicle",
  "(6)26 Unsafe Usage of a Bicycle",
  "(6)27 Carrying a invalid Operator's License",
  "(6)28 Failure to Show License to a Peace Officer",
  "(6)29 Jaywalking",
  "(6)30 Tinted Windows",
  "(6)31 Parking in a Fire Lane",
  "(6)32 Tailing First Responders",
  "(6)33 Prohibiting Entrance of an Emergency Vehicle",
  "(6)34 Impeded Normal Activity",
  "(6)35 Improper Vehicle Lighting",
  "(6)36 Operating Commercial Vehicle without License",
  "(6)37 Improper Display of Police Lights",
  "(6)38 Interference with Traffic Control Devices",
  "(6)39 Manipulating a DOT Traffic Messaging Sign",
  "(6)40 Failure to Yield to a Road Worker",
  "(6)41 Violation of a No Pass Zone",
  "(6)42 Failure to Maintain a Safe Distance",
  "(6)43 Failure to Stop",
  "(6)44 Failure to Yield",
  "(6)45 Unattended Motor Vehicle",
  "(6)46 Unsafe Operation of Automobile Door",
  "(6)47 Improper Following of an Emergency Vehicle",
  "(6)48 Lane Splitting",
  "(6)49 Unsecured Passengers in Pickup Truck Bed",
  "(6)50 Unroad Worthy Vehicle",
  "(6)51 Unsafe Lane Change",
  "(6)52 Failure to Sign a Citation",
  "(6)53 Operation of Uninsured Motor Vehicle",
  "(6)54 Failure To Obey Move Over Law",
  "(7)01 Laundering of Money Instruments",
  "(7)02 Construction and Maintenance Code Violation",
  "(7)03 Corporate Hijacking",
  "(7)04 Interference with Operations",
  "(7)05 Sale of Alcohol or Tobacco to a Minor",
  "(7)06 Gambling Violation",
  "(7)07 Falsifying Medical Credentials",
  "(7)08 Poaching",
  "(7)09 Hunting or Fishing without a Valid License",
  "(7)10 Failure to Consent to Fire Inspection",
  "(7)11 Failure to Add Fire Protection Equipment"
]

penal_codes_cha = [
  "$1000 + 30 sec jail time",
  "$500",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "$1500 + 90 sec jail time",
  "$500 + 30 jail time",
  "$1000 + 60 sec jail time",
  "$2000 + 120 sec jail time | 2nd Degree (200 Seconds; $2500)",
  "$2500 + 150 sec jail time",
  "$2000 + 120 sec jail time",
  "$1500 + 90 sec jail time",
  "$1500 + 90 sec jail time",
  "$3000 + 210 sec jail time",
  "2500 + 180 sec jail time",
  "$1000 + 60 sec jail time | 2nd degree; 120 Seconds",
  "$1500 + 300 sec jail time",
  "$500 + 240 sec jail time",
  "$1000 + 60 sec jail time",
  "$500 + 30 secs jail time",
  "$6000 + 500 sec jail time",
  "$1000 + 60 sec jail time",
  "120 Seconds + $2000 | 250 seconds + $2500",
  "60 Seconds+$1000 | 120 seconds + $2000",
  "2500 + 180 sec jail time",
  "$1500 + 90 sec jail time",
  "$500 + 30 sec jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 60 sec jail time",
  "$500 + 30 jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "$1500 + 90 sec jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 60 sec jail time",
  "$500 + 30 jail time",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "2500 + 180 sec jail time",
  "30 seconds + doubled original fine",
  "$250 + 60 sec jail time",
  "$750 + 120 sec jail time",
  "$1250 + 180 sec jail time",
  "$1500 + 120 sec jail time",
  "(Currency they offered) + 90 sec jail time",
  "$1000 + 60 seconds",
  "120 seconds + $750",
  "80 seconds + $1000",
  "$500",
  "60 seconds + $500",
  "45 seconds + $250",
  "120 Seconds + $750",
  "45 seconds + $250",
  "60 seconds + $350",
  "30 seconds",
  "120 seconds + $300",
  "360 seconds + $2000",
  "60 seconds + $750",
  "80 seconds + $500",
  "60 seconds",
  "120 seconds + $1000",
  "30 seconds",
  "60 seconds + $500",
  "Vehicle Impoundment + License Suspension 2 days + $500",
  "$500",
  "30 seconds",
  "$750",
  "45 seconds + $500",
  "30 seconds",
  "30 seconds + $250",
  "$500",
  "Business Revoked + 60 seconds",
  "60 seconds",
  "45 seconds + $650",
  "60 seconds",
  "75 seconds + $550",
  "160 seconds",
  "$500 + 60 seconds",
  "25 seconds",
  "20 seconds + $600",
  "60 seconds",
  "200 seconds + $500",
  "$500 + Vehicular impoundment + 60 sec jail time (officer discretion)",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "$250",
  "$500 + 30 sec jail time",
  "$1000 + 60 sec jail time",
  "$1000 + 5 Day License Suspension + 60 sec jail time",
  "$250",
  "$500",
  "$750",
  "$1,000",
  "$500 + Vehicular Impoundment",
  "$250",
  "$250",
  "$500",
  "$250",
  "$500",
  "$250",
  "$750",
  "$500",
  "$250",
  "$250",
  "$1000 + 60 sec jail time",
  "$1500 + 90 sec jail time",
  "$500 + Vehicular Impoundment (officer discretion)",
  "$250",
  "$1000 + Vehicular impoundment + 60 sec jail time (officer discretion)",
  "$1000 + 60 sec jail time",
  "$250",
  "$250",
  "$500 + Vehicular impoundment",
  "$500 + Vehicular Impoundment (officer discretion)",
  "$500 + Vehicular impoundment",
  "$500",
  "$250",
  "$500 + Vehicular impoundment",
  "$1000 + Vehicular impoundment + 60 sec jail time (officer discretion)",
  "$500",
  "$500",
  "$750",
  "$500 + Vehicular Impoundment (officer discretion)",
  "$500",
  "$250",
  "$250",
  "$750",
  "$250",
  "$500 + Vehicular Impoundment (officer discretion)",
  "$500",
  "$1,000",
  "$1000 + Vehicular Impoundment",
  "$250",
  "30 seconds",
  "$250 + Vehicular Impoundment",
  "$5,000",
  "$1500 + 90 sec jail time",
  "$500",
  "45 seconds + $1000",
  "$750",
  "30 seconds + $1250",
  "$500",
  "60 seconds",
  "$1,000",
  "$250",
  "$500 + Business Closed 24 hours",
  "$150 + Business Closed 48 hours"
]


async def autocomp(
  option: hikari.CommandInteractionOption, interaction: hikari.AutocompleteInteraction
) -> list[str]:
  # The `option` argument is the current text that the user typed in.
  if not isinstance(option.value, str):
      # This will raise a TypeError if `option.value` cannot be converted
      option.value = str(option.value)

  # You can query a database, fetch an api, or return any list of strings
  # Here, you might want to dynamically fetch options based on the user's input
  penal_codes_ref = [
    "(1)01 Intimidation (Major)",
    "(1)02 Intimidation (Minor)",
    "(1)03 Assault",
    "(1)04 Assault on LEO / Gov. Worker",
    "(1)05 Aggravated Assault",
    "(1)06 Battery",
    "(1)07 Aggravated Battery",
    "(1)08 Attempted Murder",
    "(1)09 Attempted Murder on LEO / Gov. Worker; 1st Degree",
    "(1)10 Attempted Murder; 2nd Degree",
    "(1)11 Voluntary Manslaughter",
    "(1)12 Criminally Negligent Homicide",
    "(1)13 Murder; 1st Degree",
    "(1)14 Murder; 2nd Degree",
    "(1)15 False Imprisonment",
    "(1)16 Aggravated Kidnapping",
    "(1)17 Simple Kidnapping",
    "(1)18 Robbery; 1st Degree",
    "(1)19 Robbery; 2nd Degree",
    "(1)20 Human Trafficking",
    "(1)21 Criminal Threats",
    "(2)01 Arson; 1st Degree",
    "(2)02 Arson; 2nd Degree",
    "(2)03 Reckless Burning; Felony",
    "(2)04 Reckless Burning; Misdemeanor",
    "(2)05 Trespassing",
    "(2)06 Trespassing within a Restricted Facility",
    "(2)07 Aggravated Trespassing",
    "(2)08 Burglary; 1st Degree",
    "(2)09 Burglary; 2nd Degree",
    "(2)10 Possession of Burglary Tools",
    "(2)11 Petty Theft",
    "(2)12 Theft",
    "(2)13 Grand Theft",
    "(2)14 Grand Theft Auto",
    "(2)15 Grand Theft of a Firearm",
    "(2)16 Receiving/Possession of Stolen Property",
    "(2)17 Extortion",
    "(2)18 Forgery",
    "(2)19 Fraud",
    "(2)20 Vandalism",
    "(2)21 Manufacturing Forged Documents",
    "(2)22 Manufacturing Forged Gov. Documents",
    "(2)23 Failure to Pay Fine",
    "(2)24 Destruction of Civilian/Private Property; 1st Degree",
    "(2)25 Destruction of Civilian/Private Property; 2nd Degree",
    "(2)26 Destruction of Civilian/Private Property; 3rd Degree",
    "(2)27 Destruction of Government Property",
    "(3)01 Bribery",
    "(3)02 Witness Tampering",
    "(3)03 False Information; 1st Degree",
    "(3)04 False Information; 2nd Degree",
    "(3)05 Filing a False Complaint",
    "(3)06 Impersonating a Government Official; Implied",
    "(3)07 Impersonating a Government Official; Deceiving",
    "(3)08 Impersonating a Government Official; Fraud",
    "(3)09 Failure to Identify to a Peace Officer",
    "(3)10 Obstruction of Justice",
    "(3)11 Resisting a Peace Officer; without Violence",
    "(3)12 Resisting a Peace Officer; with Violence",
    "(3)13 Escape from Custody",
    "(3)14 Tampering with Evidence",
    "(3)15 Conveyance within a Government Facility",
    "(3)16 Violation of Parole or Probation",
    "(3)17 Corruption from Public Duty",
    "(4)01 Disturbing the Peace",
    "(4)02 Incitement to Riot or Cause Violence",
    "(4)03 Street Racing",
    "(4)04 Refusal to Remove Facial Obstruction",
    "(4)05 Facial Obstruction whilst Committing a Crime",
    "(4)06 Disorderly Conduct",
    "(4)07 Interference with Government Operations",
    "(5)01 Possession of a Controlled Substance",
    "(5)02 Possession of a Controlled Substance with Intent to Sell",
    "(5)03 Possession of Drug Paraphernalia",
    "(5)04 Maintaining a Place for the Purpose of Distribution",
    "(5)05 Manufacture or Sale of a Controlled Substance",
    "(5)06 Possession of an Open Container",
    "(5)07 Public Intoxication",
    "(5)08 Animal Cruelty; Animal Abuse",
    "(5)09 Wanton Endangerment",
    "(5)10 Minor Alcohol Violation",
    "(5)11 Restricted Possession of a Firearm",
    "(5)12 Brandishing of a Firearm",
    "(5)13 Negligent Discharge of a Firearm",
    "(5)14 Drive-by Shooting; Shooting from a Vehicle",
    "(6)01 Driving with a Suspended/No License",
    "(6)02 Evading a Peace Officer",
    "(6)03 Reckless Evasion of a Peace Officer",
    "(6)04 Excessive Noise Violation",
    "(6)05 Hit & Run",
    "(6)06 Reckless Operation of Vehicle",
    "(6)07 Reckless Operation of Vehicle Causing Bodily Harm",
    "(6)08 3rd degree Speeding Violation",
    "(6)09 2nd Degree Speeding Violation",
    "(6)10 1st Degree Speeding Violation",
    "(6)11 Excessive Speeding Violation",
    "(6)12 Use of Nitrous Oxide",
    "(6)13 Failure to Stop",
    "(6)14 Lane Violation",
    "(6)15 Ignoring Traffic Signs",
    "(6)16 Disregard for Road Work",
    "(6)17 Failure to follow flow of traffic",
    "(6)18 Failure to Yield at an Intersection",
    "(6)19 Failure to Yield to a Pedestrian",
    "(6)20 Failure to Yield to Emergency Vehicles",
    "(6)21 Parking Violation",
    "(6)22 Impeding Traffic",
    "(6)23 Driving Under the Influence; Over Legal Limit",
    "(6)24 Driving Under the Influence; Drugs",
    "(6)25 Failure to Register a Vehicle",
    "(6)26 Unsafe Usage of a Bicycle",
    "(6)27 Carrying a invalid Operator's License",
    "(6)28 Failure to Show License to a Peace Officer",
    "(6)29 Jaywalking",
    "(6)30 Tinted Windows",
    "(6)31 Parking in a Fire Lane",
    "(6)32 Tailing First Responders",
    "(6)33 Prohibiting Entrance of an Emergency Vehicle",
    "(6)34 Impeded Normal Activity",
    "(6)35 Improper Vehicle Lighting",
    "(6)36 Operating Commercial Vehicle without License",
    "(6)37 Improper Display of Police Lights",
    "(6)38 Interference with Traffic Control Devices",
    "(6)39 Manipulating a DOT Traffic Messaging Sign",
    "(6)40 Failure to Yield to a Road Worker",
    "(6)41 Violation of a No Pass Zone",
    "(6)42 Failure to Maintain a Safe Distance",
    "(6)43 Failure to Stop",
    "(6)44 Failure to Yield",
    "(6)45 Unattended Motor Vehicle",
    "(6)46 Unsafe Operation of Automobile Door",
    "(6)47 Improper Following of an Emergency Vehicle",
    "(6)48 Lane Splitting",
    "(6)49 Unsecured Passengers in Pickup Truck Bed",
    "(6)50 Unroad Worthy Vehicle",
    "(6)51 Unsafe Lane Change",
    "(6)52 Failure to Sign a Citation",
    "(6)53 Operation of Uninsured Motor Vehicle",
    "(6)54 Failure To Obey Move Over Law",
    "(7)01 Laundering of Money Instruments",
    "(7)02 Construction and Maintenance Code Violation",
    "(7)03 Corporate Hijacking",
    "(7)04 Interference with Operations",
    "(7)05 Sale of Alcohol or Tobacco to a Minor",
    "(7)06 Gambling Violation",
    "(7)07 Falsifying Medical Credentials",
    "(7)08 Poaching",
    "(7)09 Hunting or Fishing without a Valid License",
    "(7)10 Failure to Consent to Fire Inspection",
    "(7)11 Failure to Add Fire Protection Equipment"
  ]

  # Filter options based on user input
  filtered_options = [lang for lang in penal_codes_ref if option.value.lower() in lang.lower()]

  # If there are more than 25 filtered options, adjust the page number automatically
  page_size = 25
  page_number = max(1, (len(filtered_options) - 1) // page_size + 1)

  # Paginate the options to display only 25 options per page
  start_index = max(0, (page_number - 1) * page_size)
  end_index = min(len(filtered_options), start_index + page_size)
  page_options = filtered_options[start_index:end_index]

  # If there are more options beyond this page, include an option to navigate to the next page
  if end_index < len(filtered_options):
      page_options.append("More options available. Continuing on next page...")

  return page_options



@plugin.command
@lightbulb.option('charge4', 'charge4', required=False, autocomplete=autocomp)
@lightbulb.option('charge3', 'charge3', required=False, autocomplete=autocomp)
@lightbulb.option('charge2', 'charge2', required=False, autocomplete=autocomp)
@lightbulb.option('dep', 'what department', choices=['Outagamie County Sheriff\'s Office', 'Wisconsin State Patrol'], required=True)
@lightbulb.option('charge1', 'what charge', required=True, autocomplete=autocomp)
@lightbulb.option('user', 'what user', type=hikari.Member, required=True)
@lightbulb.command('ticket', 'ticket a user')
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd(ctx):
    db = client.get_database('data')
    license = None
    records = db.ticketing
    user = ctx.options.user

    def get_first_word(input_string):
        words = input_string.split()
        if words:
            return words[0]
        else:
            return None

    charge1 = ctx.options.charge1
    charge2 = ctx.options.charge2
    charge3 = ctx.options.charge3
    charge4 = ctx.options.charge4
    try: 
      charge1_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge1))]
      charge1_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge1))]
    except Exception:
      charge1_ind = charge1
      charge1_pro = charge1
      pass
    try:
        charge2_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge2))]
        charge2_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge2))]
    except Exception:
        charge2_pro = ""
        charge2_ind = ""
        pass
    try:
        charge3_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge3))]
        charge3_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge3))]
    except Exception:
        charge3_pro = ""
        charge3_ind = ""
        pass

    try:
        charge4_pro = penal_codes_cha[penal_codes_cod.index(get_first_word(charge4))]
        charge4_ind = penal_codes_cod[penal_codes_cod.index(get_first_word(charge4))]
    except Exception:
        charge4_pro = ""
        charge4_ind = ""
        pass
      
    charges = charge1_ind + " " + charge2_ind + " " + charge3_ind + " " + charge4_ind + " "
    due = charge1_pro + " + " + charge2_pro + " + " + charge3_pro + " + " + charge4_pro
    resp = records.find_one({'user_id': user.id})
    if ctx.options.dep == "Outagamie County Sheriff\'s Office":
        prefix = "Deputy "
    if ctx.options.dep == "Wisconsin State Patrol":
        prefix = "Trooper "
    if ctx.options.dep == "FVMPD":
        prefix = "Officer "
    if resp is None:
        records.insert_one({
            'user_id': user.id,
            'citations': [{
                'Charges': charges,
                'Ticketed by': f"{prefix}<@{ctx.author.id}>",
                'Department': ctx.options.dep,
                'Amount due': f"Due: {due}"
            }],
            'vehicles': [],
            'license': False
        })
        dm_channel = bo.cache.get_dm_channel_id(user.id) # from cache
        dm_channel = await bo.rest.create_dm_channel(user.id) # from rest api; more reliable. store this for later uses
        ...
  
        # when you want to send the message
        emb = hikari.Embed(
          title="Citation Recieved",
          description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
          color="#2a2d31"
        )
        await dm_channel.send(embed=emb)
        emb = hikari.Embed(
          title="Citation Sent",
          description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
          color="#2a2d31"
        )
        await ctx.respond(embed=emb, flags=hikari.MessageFlag.EPHEMERAL)
        return
    upd = {
      'Charges': charges,
      'Ticketed by': f"{prefix}<@{ctx.author.id}>",
      'Department': ctx.options.dep,
      'Amount due': f"Due: {due}"
}
    records.update_one({'user_id': user.id}, {'$push': {'citations':upd}})
    dm_channel = bo.cache.get_dm_channel_id(user.id) # from cache
    dm_channel = await bo.rest.create_dm_channel(user.id) # from rest api; more reliable. store this for later uses
    ...
  
    # when you want to send the message
    emb = hikari.Embed(
      title="Citation Recieved",
      description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
      color="#2a2d31"
    )
    await dm_channel.send(embed=emb)
    emb = hikari.Embed(
      title="Citation Sent",
      description=f"Penal Codes: **{charges}**\nDepartment: {ctx.options.dep}\nOfficer: {prefix}<@{ctx.author.id}>\nDue: {due}",
      color="#2a2d31"
    )
    await ctx.respond(embed=emb, flags=hikari.MessageFlag.EPHEMERAL)



def load(bot):
    global bo
    bo = bot
    bot.add_plugin(plugin)
    print("Successfully loaded")
