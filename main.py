import basics.output.simple_message as simple_message

import basics.output.multiline_message as multiline_message

def run_block_a():

  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()

  #Selected options
    #Run basics.output.simple_message as simple_message
  if (response == "simple_message"):
    simple_message.run()
    # Run basics.output.multiline_message as multiline_message
  elif (response == "multiline_message"):
    multiline_message.run()


def run():
  is_running = True

  while(is_running):
    print("\nWhat would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[q] Quit")
    response = input()

    #Run function run_block_a()
    if (response == "a"):
      run_block_a()

    #Quit the prograù
    elif (response == "q"):
      break

    else:
      print("Invalid option! Please try again.")

run()