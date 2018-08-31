1. Build the image: `docker build -t test-mlflow .`
2. Run the image: `docker run --rm -it -p 8889:8888 -v $PWD:/home/jovyan/work/ jupyter/minimal-notebook start-notebook.sh --NotebookApp.token=''` from the root directory.
3. Open the notebook and execute cells.
3. In another terminal run `mlflow ui` from the root of the cloned project.
3. After each cell execution refresh the `mlflow` view and notice that the line is overwritten!
