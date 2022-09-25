from predicate_definition import PredicateDefinition

do_loc = True 
do_rad = False 
locs = ['pipes']
property = 'F pipes'

predDef = PredicateDefinition(do_loc,do_rad,locs,property)

def abstract_message(message):
    return predDef.process_message(message)