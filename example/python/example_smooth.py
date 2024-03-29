from QCARWorkflow.qcaw import Workflow, User, Dataset

client = User(user = "User1", password = "1234").server()

print("The list of dataset\n", client.list_collections()) # This will print all the dataset the User1 has.

ds = Dataset("HCN", ds_type = "OptimizationDataset", client=client).setting("load") # loading an OptimizationData set named 'test'.
Workflow(ds = ds, client = client, spec_name = "HCN", initial = "HCN.xyz").smoothing() # Workflow class and smoothing function



# We can submit another set of molecules with a new data set

ds_2 = Dataset("H2O_proton", ds_type = "OptimizationDataset", client=client).setting("load")
Workflow(ds = ds_2, client = client, spec_name = "H2O_proton", initial = "H2O_proton.xyz").smoothing()
















