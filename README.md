# ROSMonitoring 

ROSMonitoring is a framework developed for verifying at runtime the messages exchanged in a ROS system.
The repository contains the Python implementation for integrating RML (Runtime Monitoring Language, https://rmlatdibris.github.io/) verification and ROS (https://www.ros.org/). Through instrumentation, it is generated a node monitor in ROS which is able to percept the messages exchanged by the other nodes. In the online application, upon each message reception, the monitor will send a corresponding Json message to a oracle, which has been implemented in this case through a Webserver Prolog attached to an RML specification. In the offline application, the monitor will simply generate a log file which can be easily analyzed later on (in this case always through Prolog and RML). ROSMonitoring is easily extendable anyway to new formalisms; it requires only an oracle Webserver using Websockets ready to receive Json messages generated by the ROS node monitor. In the current implementation, the Webserver is written in SWI-Prolog and, upon a message reception, queries an RML specification.

# Prerequisities

ROSMonitoring works only for ROS distributions >=Groovy Galapagos.

## Pip (https://pypi.org/project/pip/)
On Ubuntu 18.04 would be:
```bash
$ sudo apt install pip
```
For other distributions, or if this command does not work, follow the instructions at the link reported above.

Using pip we can then install the Python libraries we need.
```bash
$ pip install websocket_client
$ pip install rospy_message_converter
```
## Prolog (http://www.swi-prolog.org/build/PPA.html):
```bash
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:swi-prolog/stable
$ sudo apt-get update
$ sudo apt-get install swi-prolog
```

## Java (https://openjdk.java.net/install/):
The following instructions are for installing OpenJDK-11.
```bash
$ sudo add-apt-repository ppa:openjdk-r/ppa
$ sudo apt-get update
$ sudo apt-get install openjdk-11-jdk
```

# How ROSMonitoring is organized

This repository contains two folders:
 - generator
 - oracle
 - monitor

# Generator

The generator folder contains the generator program (Python). It can be used for instrumenting a ROS project (where the nodes are implemented in Python) and generating a monitor node for achieving the Runtime Verification of our ROS nodes.
This generator program takes a configuration file in input (the config.yaml contained in the same folder). Using this simple configuration file we can customize the generation of our monitors and how the ROS nodes will be instrumented.

# Oracle

The oracle folder contains two subfolders: prolog and rml

The Prolog folder contains the prolog files implementing the semantics of the specification language chosen: RML.
In this folder we can find the semantics of the Trace Expression formalism (the lower level calculus obtained compiling RML specifications). Beside the semantics, we have the implementation of a monitor in Prolog, both for Online and Offline RV. The Online RV is achieved through the use of Websockets; the monitor in Prolog consists in a Webserver listening on a chosen url and port. The ROS monitor generated through instrumentation will communicate the observed events at Runtime through this websocket connection. The Offline implementation is simpler, it simply consists in a Prolog implementation where a log file can be analysed offline (after the execution of the ROS system). Also in this case, the events checked by the monitor are obtained by the ROS monitor, which in the Offline scenario logs the observed events inside a log file. The same log file will be later analysed by the prolog monitor.

The other folder contains example of specifications using RML.

# How to use ROSMonitoring (through an example extracted by ROS Tutorial)

First things first..
Before going on we need a machine with ROS installed. It is not important which ROS distribution, as long as rospy is supported.

In the following we are going to use ROS Melodic with Catkin on Ubuntu 18.04, but as mentioned before, you can use any distribution starting from Groovy Galapagos.

## Install ROS Melodic

http://wiki.ros.org/melodic/Installation

## Create a workspace for catkin

http://wiki.ros.org/catkin/Tutorials/create_a_workspace

## Create ROS package

http://wiki.ros.org/ROS/Tutorials/CreatingPackage

We need the 'beginner_tutorials' package, so do not forget to create it!

## Writing simple Publisher and Subscriber using rospy

http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

At the end of this tutorial you should have the talker and listener node working.
To run the example, follow the instructions at:

http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber

At the end of the tutorial, the talker and listener nodes should be able to communicate freely.

In order to simplify the monitoring process and make it easier, we need to change a small thing inside talker.py.

Line 47 must become:
```python
...
hello_str = "hello"
...
```

The last thing to do is to add a launch file for running our nodes.
Create a launch file called 'run.launch' inside the 'beginner_tutorials' folder, and paste the following XML inside it.
```xml
<launch>
    <node pkg="beginner_tutorials" type="talker.py" name="talker" output="screen"/>
    <node pkg="beginner_tutorials" type="listener.py" name="listener" output="screen"/>
</launch>
```

Now we are ready to start monitoring our talker and listener nodes!

## Clone the ROSMonitoring repository

We need the ROSMonitoring implementation in order to instrument and verify our nodes. So, now is the time to clone the repository, if you have not already.

In the terminal:
```bash
 $ cd ~/
 $ git clone https://github.com/autonomy-and-verification-uol/ROSMonitoring.git
```
Now you should have your local ROSMonitoring folder.

### Create a simple Offline monitor

The creation of a monitor is extremely flexible, and we can easily customize how many monitors, what they can do, and above all, what they are going to check (which topics, and so on).
For customizing the monitors, we use a YAML configuration file. You can find different ones we already prepared for you for exploring ROSMonitoring in the Talker-Listener example.

The first we are going to see is: 'offline_config.yaml'

```yaml
nodes: # here we list the nodes we are going to monitor
  - node:
      name: talker
      package: beginner_tutorials
      path: ~/catkin_ws/src/beginner_tutorials/run.launch
  - node:
      name: listener
      package: beginner_tutorials
      path: ~/catkin_ws/src/beginner_tutorials/run.launch

monitors: # here we list the monitors we are going to generate
  - monitor:
      id: monitor
      log: ./log.txt # file where the monitor will log the observed events
      silent: False # we let the monitor to print info during its execution
      topics: # the list of topics this monitor is going to intercept (only one here)
        - name: chatter # name of the topic
          type: std_msgs.msg.String # type of the topic
          action: log # the monitor will log the messages exchanged on this topic 
```

This configuration file informs the generator about two nodes: talker and listener. Along with important information concerning their package and where we can find the corresponding launch file (which is the one we created previously).  

Now we can run the generator passing this configuration file in the following way. 

```bash
$ cd ~/ROSMonitoring/generator/
$ chmod +x generator
$ ./generator --config_file offline_config.yaml
```

Going back to the 'ROSMonitoring' folder, if we look into the 'monitor/src/' folder, we will find a new generated Python script called 'monitor.py'. This file contains the code for the monitor.
Inside 'beginner_tutorials' we can also find now a new launch file called 'run_instrumented.launch'.

Now, if we want to run our ROS nodes with the new monitor together, we have to just copy the monitor folder under 'catkin_ws/src'. Since we are adding a new ROS package (the monitor package), we need also to re-run the catkin_make command.

Now we have everything we need to run the system along with the monitor.

In a terminal we do:

```bash
$ cd ~/catkin_ws/
$ roslaunch src/monitor/run.launch
```

Then, in another terminal we do:

```bash
$ cd ~/catkin_ws/
$ chmod +x src/monitor/src/monitor.py
$ roslaunch src/beginner_tutorials/run_instrumented.launch
```

You should not notice any difference, even though now we have a monitor running along with the two other nodes.
What is it actually happening? We have created and run an offline monitor. If we stop the nodes and the monitor, we should see that a new file has been created inside 'catkin_ws', called 'log.txt' (as we set in the config file).

We can find the automatically generated log file (log.txt) inside ~/catkin_ws folder.

The log file should look like this:
```json
{"topic": "chatter", "data": "hello", "time": 1559638159.43485}
{"topic": "chatter", "data": "hello", "time": 1559638159.534461}
{"topic": "chatter", "data": "hello", "time": 1559638159.635648}
...
```

The so generated log file can be parsed by any runtime monitor, as long as the latter supports events formatted using Json.
The default Oracle for ROSMonitoring is implemented in SWI-Prolog and supports the RML formalism.

The last step for the Offline version is to check the log file against a formal specification.
To do this, first we copy the log file into the prolog folder, and then we run the monitor (using the already given sh file).
```bash
$ cp ~/catkin_ws/log.txt ~/ROSMonitoring/oracle/
$ cd ~/ROSMonitoring/oracle/prolog/
$ sh offline_monitor.sh ../rml/test.pl ../log.txt
...
matched event #89
matched event #90
matched event #91
matched event #92
Execution terminated correctly
```

offline_monitor.sh expects two arguments:
 - the specification we want to verify (test.pl in this example)
 - the log file containing the traces generated by the ROS monitor (log.txt in this case)

The test.pl is the lower level representation of test.rml (contained in the same folder). If we want to verify new properties, we only need to write them followin the RML syntax (creating a corresponding .rml file). And then, we can compile the new rml specifications using the rml-compiler.jar (also contained in the rml folder).

For instance, to generate test.pl, we can do as follows:
```bash
$ cd ~/ROSMonitoring/oracle/rml/
$ java -jar rml-compiler.jar --input test.rml --output test.pl
```
The compiler will automatically compile the rml file into the equivalent prolog one, which can be used directly from the Prolog monitor.
More information about RML can be found at: https://rmlatdibris.github.io/


### Adding a monitor in the middle.

In the previous example we saw how to generate a monitor which logs the intercepted events. In that scenario we can achieve in this way offline RV, because we are analyzing previously generated traces. But, with ROSMonitoring we can do much more than that. We can create a monitor which achieves online RV, meaning that the analysis is done while the system is running.

Let's have a look at the other configuration file called: 'online_config.yaml'

```yaml
nodes: # here we list the nodes we are going to monitor
  - node:
      name: talker
      package: beginner_tutorials
      path: ~/catkin_ws/src/beginner_tutorials/run.launch
  - node:
      name: listener
      package: beginner_tutorials
      path: ~/catkin_ws/src/beginner_tutorials/run.launch

monitors: # here we list the monitors we are going to generate
  - monitor:
      id: monitor
      log: ./log.txt # file where the monitor will log the observed events
      silent: False # we let the monitor to print info during its execution
      oracle: # the oracle running and ready to check the specification (localhost in this case)
        port: 8080 # the port where it is listening
        url: 127.0.0.1 # the url where it is listening
        action: nothing # the oracle will not change the message
      topics: # the list of topics this monitor is going to intercept
        - name: chatter # name of the topic
          type: std_msgs.msg.String # type of the topic
          action: filter 
          publishers:
           - talker
```

This configuration file is very similar to the previous one. But this time we are asking for the generation of an online monitor. In order to do so, we need to inform the generator where the Oracle is listening and on which port. In this way, the generated monitor will be capable of communicating with it using WebSockets.
Another addition to this configuration file is the 'publishers' field inside the chatter topic.
Since we are doing online RV, the monitor is checking the events at runtime. Now, if we wanted just to log each event, we could maintain the action set to 'log'. The behaviour in this way would be exactly the same as for the offline monitor, with the only difference that each time an event is observed, the monitor propagates this event to the oracle and waits for the current verdict against a chosen property. Consequently, rather than the offline case, in the online scenario, the monitor will also log the satisfaction/violation of the property (but nothing more). This can be useful if we are debuggin a system, but in a real scenario we could need to enforce the correcteness of the events. For instance, filtering the events which are considered wrong by the Oracle. For doing this, we can change the action from 'log' to 'filter'.

Once the action 'filter' is selected, the monitor will filter the wrong messages. But, to be able to do so, it must be in the middle of the communication. Until now the monitor was only another node in the system and was just subscribing the topics. This is not enough if we want to filter the wrong messages. In order to solve this problem, ROSMonitoring instrument the nodes changing the names and creating gaps in the communications. Thanks to this communication gaps, the monitor can become a bridge for the topics of our interest, and filter the messages in case they are wrong.

To create the gap the generator needs to know who is the publisher (or subscriber) for the topic we want ot filter. In this case we indicate 'talker', which is the publisher for the 'chatter' topic.

After that, we can simply run again the generator.

```bash
$ cd ~/ROSMonitoring/generator/
$ chmod +x generator
$ ./generator --config_file online_config.yaml
```

This will generate again a new monitor and the launch files we need.
As before, now we just have to copy the monitor folder under the catkin workspace and run catkin_make again.

Since now the monitor is online, it needs an oracle to check the events. As for the offline case, ROSMonitoring does not require any specific runtime monitor to be used as Oracle. The only requirements are having an Oracle capable of communicating through WebSockets and able to parse Json events.
Again, ROSMonitoring already have a default Oracle, which is implemented in SWI-Prolog and supports the RML formalism.

Thus, before running our Online monitor, we need to execute the Webserver Prolog, as possible implementation of our oracle.
```bash
$ cd ~/ROSMonitoring/oracle/prolog/
$ sh online_monitor.sh ../rml/test.pl 8080
% Started server at http://127.0.0.1:8080/
Welcome to SWI-Prolog (threaded, 64 bits, version 8.0.2)
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software.
Please run ?- license. for legal details.

For online help and background, visit http://www.swi-prolog.org
For built-in help, use ?- help(Topic). or ?- apropos(Word).

?-
```

After that we can do the same as for the offline case. First we run 'run.launch' for running the monitor, and then we run 'run_instrumented.launch' for running the instrumented nodes (notice that now we added the 'remap' params fro creating the gap in the communication).
The monitor will now check the events at runtime. But, since the property is always satisfied, no events will be filtered out. Changing the property you will be able to see that if the event is not consistent, it is not propagated to the subscriber node!
