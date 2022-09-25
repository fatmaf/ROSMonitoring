#used to generate a property 
batch_name = 'visit'
#"(F ipone) AND (F t2bottom) AND (F tankset) AND (F pipes)"
#"(G ! (dangerred)) AND ((!(t2bottom)) U ipone) AND ((!(tankset)) U ipone) AND ((!(pipes)) U ipone) AND ((!(pipes)) U t2bottom) AND ((!(pipes)) U tankset) AND ((!(tankset)) U t2bottom)"
properties = [
    {'type':'req','property':'F pipes', 'do_loc':True, 'do_rad':False, 'locs':['pipes']},
    {'type':'req','property':'F ipone', 'do_loc':True, 'do_rad':False, 'locs':['ipone']},
    {'type':'req','property':'F t2bottom', 'do_loc':True, 'do_rad':False, 'locs':['t2bottom']},
    {'type':'req','property':'F tankset', 'do_loc':True, 'do_rad':False, 'locs':['tankset']},
    {'type':'pref','property':'G (!(dangerred))', 'do_loc':False, 'do_rad':True, 'locs':[]},
    {'type':'pref','property':'((!(t2bottom)) U ipone)', 'do_loc':True, 'do_rad':False, 'locs':['t2bottom','ipone']},
    {'type':'pref','property':'((!(tankset)) U ipone)', 'do_loc':True, 'do_rad':False, 'locs':['tankset','ipone']},
    {'type':'pref','property':'((!(pipes)) U ipone)', 'do_loc':True, 'do_rad':False, 'locs':['pipes','ipone']},
    {'type':'pref','property':'((!(pipes)) U t2bottom)', 'do_loc':True, 'do_rad':False, 'locs':['pipes','t2bottom']},
    {'type':'pref','property':'((!(pipes)) U tankset)', 'do_loc':True, 'do_rad':False, 'locs':['pipes','tankset']},
    {'type':'pref','property':'((!(tankset)) U t2bottom)', 'do_loc':True, 'do_rad':False, 'locs':['tankset','t2bottom']}   
    
              ]

for prop in properties:
    fnprop = prop['property'].replace(' ','')
    fnprop = fnprop.replace('!','not')
    fnprop = fnprop.replace('(','')
    fnprop = fnprop.replace(')','')
    
    filename = 'pg_radiation_{0}_{1}_{2}.py'.format(batch_name,prop['type'],fnprop)
    lines = "\nfrom predicate_definition import PredicateDefinition\n\ndo_loc={doloc}\ndo_rad={dorad}\nlocs={locslist}\n\nPROPERTY=\"{propertie}\"\n\npredDef = PredicateDefinition(do_loc,do_rad,locs,property)\n\n\ndef abstract_message(message):\n\treturn predDef.process_message(message)".format(doloc=prop['do_loc'],dorad=prop['do_rad'],locslist=prop['locs'],propertie=prop['property'])
    with open(filename,'w') as f:
        f.write(lines)
        
    
    
    

    
