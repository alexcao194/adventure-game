from framework.core.singleton import Singleton
from framework.game.state.base_state import FallState

class StateMachine(Singleton):
    '''
    class StateMachine
    states: list - the list of states
    navigate between states
    '''
    states = []        
    def push(state):
        StateMachine.states.append(state)
    def pop():
        if(StateMachine.canPop()):
            StateMachine.current_state.destroy()
            StateMachine.states.pop()
    # def popUntil(name):
    #     while(StateMachine.current_state.name != name and StateMachine.canPop()):
    #         StateMachine.pop()
    def canPop():
        return StateMachine.states.__len__() > 1
    def __current_state__():
        if len(StateMachine.states) == 0:
            return FallState()
        return StateMachine.states[-1]


    
