"my_print

this is a description of the func"
function my_print(that::String)
    println("hello $that")
end

my_print("what's this")

using Plots
gr()

fig = plot([sin, cos],0,2*pi)
# display(fig)
savefig(fig, "./fig.png")