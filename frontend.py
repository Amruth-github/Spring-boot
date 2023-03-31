import streamlit as st
import requests
import json

def main():
    st.title("Spring Boot")
    with st.expander("POST Request"):
    # Display the form to submit data
        st.write("Enter the following information:")
        id_input = st.text_input("ID: ", key = "id")
        name_input = st.text_input("Name:", key = "name")
        submit_button = st.button("Submit")
    
    # When the Submit button is clicked, send a POST request to the server
        if submit_button:
            url = "http://localhost:8080/addPerson"
            data = {"id": id_input, "name": name_input}
            response = requests.post(url, json=data)
            st.success("Data written to database")
    

    with st.expander("GET Request"):
        # Display a form to retrieve the data
        st.write("Retrieve the following information:")
        id_get_input = st.text_input("ID:")
        get_button = st.button("Get Data")

        get_all = st.button("Get All")
        
        # When the Get Data button is clicked, send a GET request to the server
        if get_button:
            url = f"http://localhost:8080/getPersonbyId/{id_get_input}"
            response = requests.get(url)
            st.json(response.json())
        
        if get_all:
            url = f"http://localhost:8080/getPeople"
            response = requests.get(url)
            st.json(response.json())

    with st.expander("DELETE Request"):
        st.write("Retrieve the following information:")
        id_get_input = st.text_input("ID:", key = "id_2")
        get_button = st.button("Delete", key = "name_2")
        if get_button:
            url = f"http://localhost:8080/deleteById/{id_get_input}"
            response = requests.delete(url)
            st.success("Deleted!")

    with st.expander("UPDATE Request"):
        st.write("Retrieve the following information:")
        id_input = st.text_input("ID: ", key = "id_1")
        name_input = st.text_input("New Name:", key = "name_1")
        submit = st.button("Update")

        if submit:
            url = f"http://localhost:8080/update"
            response = requests.put(url, json = {"id": id_input, "name": name_input})
            st.success("Updated!")


if __name__ == "__main__":
    main()
