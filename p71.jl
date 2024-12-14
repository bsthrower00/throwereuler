#Ordered fractions 
goal = 3/7  #0.4285714285714286
println(goal)
highest = 0
highestI = 0
for i in 1:1000000
	global highest, highestI
	a = round(goal * i)/i 
	if a < goal
		if a > highest
			highest = a
			highestI = i
		end
	end
end
println("Best approximation: ", highest, " (", highest * highestI, "/", highestI, ")")