# Use an official Jupyter notebook image
FROM jupyter/scipy-notebook:latest

# Set the working directory
WORKDIR /home/jovyan

# Expose port for Jupyter
EXPOSE 8888

# Command to run Jupyter notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
