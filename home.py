import streamlit as st
import subprocess
import os
with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title("About")
    st.info("Select the section to RUN THROUGH PREDIFINED DATASET OR REALTIME")
def run_first_file():
    # Option 1: Set working directory explicitly
    result = subprocess.run(
        ["streamlit", "run", "C:/Lastsem/LipNet-main/app/app.py"],
        capture_output=True, text=True,
        cwd="C:/Lastsem/LipNet-main/app"
    )

    # Option 2: Use os.chdir (if script and apps in same directory)
    # os.chdir("C:/Lastsem/LipNet-main/app")
    # result = subprocess.run(["streamlit", "run", "app.py"], capture_output=True, text=True)
    # os.chdir("..")  # Change back to original directory

    return result.returncode, result.stdout

def run_second_file():
    # Option 1: Set working directory explicitly
    result = subprocess.run(
        ["streamlit", "run", "C:/Lastsem/Computer-Vision-Lip-Reading-main/live_test/app1.py"],
        capture_output=True, text=True,
        cwd="C:/Lastsem/Computer-Vision-Lip-Reading-main/live_test"
    )

    # Option 2: Use os.chdir (if script and apps in same directory)
    # os.chdir("C:/Lastsem/Computer-Vision-Lip-Reading-main/live_test")
    # result = subprocess.run(["streamlit", "run", "app1.py"], capture_output=True, text=True)
    # os.chdir("..")  # Change back to original directory

    return result.returncode, result.stdout

def main():
    st.title('Lip Reading Ai')

    st.write("Click on the buttons below to run Realtime or  Dataset")

    if st.button('Run Through Dataset'):
        return_code, output = run_first_file()
        st.write('Output:')
        if return_code == 0:
            # Option 1: Truncate output (adjust max_chars as needed)
            st.code(output[:1000])  # Display the first 1000 characters

            # Option 2: Write to file
            # with open("first_file_output.txt", "w") as f:
            #     f.write(output)
            # st.success("Output written to first_file_output.txt")
        else:
            st.error(f"An error occurred: {output}")

    if st.button('Run Through realtime'):
        return_code, output = run_second_file()
        st.write('Output:')
        if return_code == 0:
            # Option 1: Truncate output (adjust max_chars as needed)
            st.code(output[:1000])  # Display the first 1000 characters

            # Option 2: Write to file
            # with open("second_file_output.txt", "w") as f:
            #     f.write(output)
            # st.success("Output written to second_file_output.txt")
        else:
            st.error(f"An error occurred: {output}")

if __name__ == "__main__":
    main()
