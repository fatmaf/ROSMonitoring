import yaml
#used to generate a property as well as the yaml file for the monitors 
#and the list of topics to copy paste into the monitor aggregator bit 

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

def generate_name(prop):
    fnprop = prop['property'].replace(' ','')
    fnprop = fnprop.replace('!','not')
    fnprop = fnprop.replace('(','')
    fnprop = fnprop.replace(')','')
    return fnprop

def generate_fullname(prop):
    fnprop = generate_name(prop)
    fn = 'pg_radiation_{0}_{1}_{2}'.format(batch_name,prop['type'],fnprop)
    return fn


def create_monitor_dict(prop,logloc,portnum):
    
    id = 'monitor_'+generate_fullname(prop)
    log = logloc+'/'+id+'.txt'
    silent = False 
    warning = 1 
    oracle = {'port':portnum,'url':'127.0.0.1','action':'nothing'}
    topics = []
    if prop['do_loc']:
        topic = {'name': 'at_location', 'type': 'std_msgs.msg.String', 'action': 'filter', 'publishers': ['monitor_resources']}
        topics.append(topic)
    if prop['do_rad']:
        topic = {'name': 'radiation_status', 'type': 'std_msgs.msg.String', 'action': 'filter', 'publishers': ['monitor_resources']}
        topics.append(topic)
        
    mondict={
        'id':id,
        'log':log,
        'silent':silent,
        'warning':warning,
        'oracle':oracle,
        'topics':topics
        }
    
    return mondict

def generate_properties_files(properties):
    for prop in properties:        
        filename = generate_fullname(prop)+'.py'
        lines = "\nfrom predicate_definition import PredicateDefinition\n\ndo_loc={doloc}\ndo_rad={dorad}\nlocs={locslist}\n\nPROPERTY=\"{propertie}\"\n\npredDef = PredicateDefinition(do_loc,do_rad,locs,property)\n\n\ndef abstract_message(message):\n\treturn predDef.process_message(message)".format(doloc=prop['do_loc'],dorad=prop['do_rad'],locslist=prop['locs'],propertie=prop['property'])
        with open(filename,'w') as f:
            f.write(lines)
        

def create_tmux_file(commands):
    with open('start_oracles.sh','w') as f:
        f.write('#!/bin/bash\n\n')
        sessionname = 'rosmon_oracles'
        f.write('\ntmux new-session -d -s {0}\n\n'.format(sessionname))
        for i in range(len(commands)):
            f.write('\ntmux new-window -n prop{0} -t {1}:'.format(i,sessionname))
            
        f.write('\n')
        for i in range(len(commands)):
            f.write('\ntmux send-keys -t {sn}:{wname} "{com}" ENTER'.format(sn=sessionname,wname='prop{0}'.format(i),com=commands[i]))
        f.write('\n')    
        f.write('\ntmux attach-session -t {sn}:{wname}'.format(sn=sessionname,wname='prop0'))
            
#for now i'm hard coding some of the stuff
def generate_generator_file(properties):
    nodes =  [{'node': 
          {'name': 'monitor_resources', 'package': 'navigation_playground', 'path': '/home/fatma/work/code/ros/ros1/rad_ws/src/navigation_playground/launch/run_monitor_resources.launch'}
          }]
    genfile = {'nodes':nodes}
    onlinecommands = []
    logloc = '/home/fatma/work/code/ros/ros1/rad_ws'
    defaultport = 8080
    monitors = []
    monnames = {'req':[],'pref':[]}
    for i in range(len(properties)):
        prop = properties[i]
        portnum = defaultport +i
        monitor = create_monitor_dict(prop, logloc, portnum)
        com = './oracle.py --online --property {0} --port {1}'.format(generate_fullname(prop),portnum)
        onlinecommands.append(com)
        monitors.append({'monitor':monitor})
        monnames[prop['type']].append(monitor['id'])
        
    genfile['monitors']=monitors
    
    with open('pg_radiation_{0}_online_config.yaml'.format(batch_name),'w') as f:
        yaml.dump(genfile,f)
    
    print("monitor names:")
    print("req")
    print(monnames['req'])
    print("pref")
    print(monnames['pref'])
    print("monitor commands:")
    create_tmux_file(onlinecommands)
    for com in onlinecommands:
        print(com)    

    
if __name__ == "__main__":
    generate_properties_files(properties)
    generate_generator_file(properties)
    
        
        
        
    

        
            
    
    

    
