import streamlit as st
import os
import time
from colorama import Fore, Style
from openai import OpenAI
from config.toastalerts import toast_alert_start, toast_alert_end, toast_alert_waiting

def app_create_slides(varTopic):
    toast_alert_start("Creating PowerPoint slides! Please wait...")
    client = OpenAI(api_key=st.secrets.openai.api_key)

    assistant_name = "PowerPoint Generator by ChatGPT code interpreter"
    output_file_name = "Presentation.pptx"
    # Updated instruction to reflect the requirement for more than 12 slides
    assistant_instruction = r"Generate a {} file with more than 12 slides, ensuring each slide is engaging and informative. As a subject-matter expert and professional PowerPoint creator, use modern and easy-to-read backgrounds, colors, fonts, and styling. Include engaging content and make the file available for download.".format(output_file_name)
    # Enhanced prompt template for clarity and effectiveness
    prompt_template = "Create a detailed presentation on '{}'. The presentation should contain at least 12 slides to ensure comprehensive coverage of the topic. Break down the content into several sections, providing detailed insights and useful information for training and sharing purposes. Include engaging and modern visuals where important, and ensure the design is clean and professional to facilitate easy reading and comprehension."

    slides_topic = varTopic
    prompt_user = prompt_template.format(slides_topic)  # Use .format for consistency and readability

    def check_run(client, thread_id, run_id):
        while True:
            # Refresh the run object to get the latest status
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run_id
            )

            if run.status == "completed":
                print(f"{Fore.GREEN}Run is completed.{Style.RESET_ALL}")
                break
            elif run.status == "expired":
                print(f"{Fore.RED}Run is expired.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.YELLOW}OpenAI: Run is not yet completed. Waiting...{run.status}{Style.RESET_ALL}")
                toast_alert_waiting("Slide creation is in progress! Please continue to wait...")
                time.sleep(5)  # Wait for 5 seconds before checking again
                

    # Create assistant
    assistant = client.beta.assistants.create(name=assistant_name, instructions=assistant_instruction, tools=[{"type": "retrieval"}, {"type": "code_interpreter"}], model="gpt-4-1106-preview")

    # Create thread, and create a message in the thread
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(thread_id=thread.id, role="user", content=prompt_user)

    # Run the thread message
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)

    # Check running status
    check_run(client, thread.id, run.id)

    # Get response message
    messages = client.beta.threads.messages.list(thread_id=thread.id)

    file_path = messages.data[0].content[0].text.annotations[0].file_path.file_id
    file_x = client.files.with_raw_response.content(file_path)

    with open(output_file_name, "wb") as file:  # Open the file in binary write mode
        file.write(file_x.content)

    with open(output_file_name, "rb") as file:
        btn_download = st.download_button(
            label="Download PowerPoint",
            data=file,
            file_name=output_file_name
        )
    # Download the file
