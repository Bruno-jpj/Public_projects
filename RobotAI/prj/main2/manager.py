import requests, time, json, sys


from agent import Agent
from simulation import Simulation
from BFT_Alg import Bft

import map_logic as ml

import matplotlib
matplotlib.use("Qt5Agg")  # oppure "Qt5Agg" se hai PyQt5 installato
import matplotlib.pyplot as plt

# Server URL to fetch commands from
URL = "http://127.0.0.1:8000/send_command/"

# check connection
def CheckData():
    n_process = 0
    try:
        r = requests.get(URL)
        r.raise_for_status() # Raise error for bad status codes - HTTPError
        data = r.json()
        
        print(f"Num-Process: [{n_process}]")
        n_process += 1

        print(f"Data received: {data}")
        print(f"Full response: {r.text}")
        print(f"Request Status Code: {r.status_code}")
        #
    except requests.exceptions.InvalidJSONError as ijs:
        print(f"Invalid JSON Error: [{ijs}]")
    except requests.exceptions.ConnectionError as ce:
        print(f"Connection Error: [{ce}]")
    except requests.exceptions.Timeout as to:
        print(f"Timeout Error: [{to}]")
    except requests.exceptions.HTTPError as http:
        print(f"HTTP Error: [{http}]")
    except ValueError as ve:
        print(f"JSON Parse Error: [{ve}]")
    except Exception as e:
        print(f"Unexpected Exception: [{e}]")
    #
    time.sleep(2)
    #
    if not data:
        pass
    #
    return data
#
def start_agent(*args): # *args: tupla | **kwargs: dict
    while True:
        # state_old = args[0].get_state(args[1]) -> corretto, ma meglio fare unpack
        if len(args) not in (1, 9):
            sys.exit("Numero argomenti non valido")
        #
        if len(args) == 1:
            flag = args
            if flag:
                break
        #
        if len(args) != 9:
            raise TypeError("Numero Argomenti non valido")
        #
        agent, simulation, reward, record, tot_reward, score, flag, fig, ax = args # unpack
        # 
        state_old = agent.get_state(simulation) # current state
        final_move = agent.get_action(state_old) # action
        reward, score = simulation.step(final_move) # exectute action
        #
        update_map(simulation, ax)
        #
        state_new = agent.get_state(simulation) # new state
        agent.train_short_memory(state_old, final_move, reward, state_new) # train short memory
        agent.remember(state_old, final_move, reward, state_new) # save exp
        agent.train_long_memory() # train long memory
        #
        if score > record: # update score
            record = score
            agent.model.save()
        #
        tot_reward += reward
        agent.n_games += 1
        #
        loss = agent.trainer.train_step(state_old, final_move, reward, state_new)
        #
        yield reward, record, tot_reward, score, agent.n_games, loss # return: termina ed esce | yield: restituisce i valori ad ogni ciclo 
#
def update_map(simulation, ax):
    ml.draw_map(simulation.robot_map, ax, simulation.w, simulation.h)
#
# Program Start Point 
def run():
    agent = Agent()
    simulation = Simulation()
    #
    agent_reward = 0
    agent_record = 0
    agent_tot_reward = 0
    agent_score = 0
    #
    flag_end = False
    #
    plt.ion()
    fig, ax = plt.subplots()
    plt.show(block = False)
    #
    while True:
        data = CheckData()
        #
        try:
            #command_text = data.get("command")
            command_text = data["command"]
            if command_text == "Start":
                print(f"Command Start")
                agent_reward, agent_record, agent_tot_reward, agent_score, movement, loss = start_agent(agent, simulation, agent_reward, agent_record, agent_tot_reward, agent_score, flag_end, fig, ax)
                print(f"Movement: [{movement}] | Score: [{agent_score}] | Trophies: [{simulation.tot_trophies}] | Reward: [{agent_reward}] | Tot-Reward: [{agent_tot_reward}] | Loss: [{loss}]")
                #
            elif command_text == "Stop":
                print(f"Command Stop")
                # simulation.current_move = None
                flag_end = True
                start_agent(flag_end)
                #
            elif command_text and  "Move to" in command_text:
                print(f"Command Move to")
                '''
                - implementare BFT per il path finding.
                - movimento del robot con Agent (in caso di ostacoli), in caso di ostacoli ricalcolo percorso
                - nel BFT non gestisco casistica degli ostacoli in modo corretto
                '''
                x,y = input("Inserisci la posizione (x,y)")
                target = (x,y)
                bft = Bft(simulation.robot, target, simulation.obstacles)

                path = bft.search()

                if path:
                    print("Percorso trovato:")
                    print(path)

                    # stop - in caso di movimento precedente si ferma
                    simulation.current_move = None

                    # start
                    simulation.current_move = simulation.spec_move(path)
                    MoveTo()
                else:
                    print("EndPoint non raggiungibile")
            #
            elif command_text == "None": # None case
                print(f"None Command..")
            else:
                print(f"Unknown Command: [{command_text}]")
                raise ValueError("Unknown Command")
        except Exception as e:
            print(f"Exception catched: [{e}]")
        except ValueError as ve:
            print(f"Value Error: [{ve}]")
        except KeyError as ke:
            print(f"Key Error, missing key [command]: [{ke}]")
        #
        if simulation.current_move:
            MoveTo(simulation)
    #
#
def MoveTo(sim):
    try:
        next(sim.current_move)
        sim.update_ui()
    except StopIteration:
        sim.current_move = None
#
if __name__ == "__main__":
    run()