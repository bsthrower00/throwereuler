function FacSet(n)
	if n < 2
		return false 
	end
	k = n % 2 == 0 ? 1 : 2	
	facSet = Int[]
	for i in 1:k:floor(Int, sqrt(n)) + 1
		if mod(n,i) == 0 
			append!(facSet, [i, floor(n/i)])
		end
	end
	return Set(facSet)
end