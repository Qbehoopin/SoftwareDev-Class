# Flow Chart Module
# This module provides functionality to create and display flow charts.

# How to plan your flow chart and program logic:
# 1. Identify the main process or decision points.
# 2. Break down the process into smaller steps or actions.
# 3. Determine the flow of control between these steps.
# 4. Use standard flow chart symbols to represent different types of actions (e.g.,
#    rectangles for processes, diamonds for decisions, arrows for flow direction, ovals for start/end, parallelograms for input/output).
# 5. Draw the flow chart using a flow charting tool or library.
# 6. Review and refine the flow chart to ensure clarity and accuracy.
# 7. Implement the logic in code based on the flow chart structure.

#Why plan Software with Flow Charts?
# 1. Visualization: Flow charts provide a visual representation of the process, making it easier.
# 2. Clarity: They help clarify complex processes by breaking them down into simpler steps.
# 3. Communication: Flow charts facilitate communication among team members and stakeholders.
# 4. Problem-Solving: They aid in identifying potential issues and inefficiencies in the process.
# 5. Documentation: Flow charts serve as documentation for future reference and maintenance.
# 6. Planning: They assist in planning the structure and logic of software before coding begins.
# 7. Debugging: Flow charts can help in debugging by providing a clear path of execution.

#Steps to software development planning
#1. Define the problem or objective.
#2. identify inputs and outputs.
#3. Break down the process into smaller tasks or functions.
#4. Design logic flow using flow charts or pseudocode.
#5. Write the code based on the planned structure.
#6. Test the software to ensure it meets requirements.
#7. Debug and refine the code as needed.
#8. Document the code and process for future reference.
#9. Maintain and update the software as necessary.

# Example Flow Chart Creation (Pseudocode)

def create_flow_chart():

    # Pseudocode for creating a flow chart
    flow_chart = []
    
    # Start (Oval)
    flow_chart.append("Start")
    
    # Input (Parallelogram)
    flow_chart.append("Input: Get user data")
    
    # Process (Rectangle)
    flow_chart.append("Process: Validate data")
    
    # Decision (Diamond)
    flow_chart.append("Decision: Is data valid?")
    
    # If Yes (Rectangle)
    flow_chart.append("Yes: Process data")
    
    # If No (Rectangle)
    flow_chart.append("No: Show error message")
    
    # End (Oval)
    flow_chart.append("End")
    
    return flow_chart

# def display_flow_chart(flow_chart):
#     for step in flow_chart:

def display_flow_chart(flow_chart):
    for step in flow_chart:
        print(step)
        

