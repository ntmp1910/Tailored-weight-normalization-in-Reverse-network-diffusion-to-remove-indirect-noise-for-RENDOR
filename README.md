
# RENDOR method for removing indirect noise with Tailored weight normalization



## Authors
- Trong Minh Phuong Nguyen: phuong.ntm225992@sis.hust.edu.vn
- Duc Tinh Pham tinhpd020780@gmail.com




## How to Run
# function.R
Contains most of the functions needed to carry out the operation.
# RandomEdgeFunction
Used to generate Indirect Edges mention in the paper.
# testevalu.R and testgensimu.R 
Additional test for the model. Currently in testing, could be use for future research.
# MainExecution
First, execute all the code from #start setup to #end setup to setup environment for the model

Run 1 of 2 Data Input function: HGRN DI or CancerSignal DI
Optional: Run the Plotting function under the DI function to see the Gene Matrix.

The proceed to Run the corresponding Indirect Edges Input function to input Indirect Edges into the Gene Matrix.
Optional: Plotting function for the Gene Matrix with Indirect Edges.

After that, Run which ever denoising model you like. and Run the Result Ploting Function as instructed to see result.
