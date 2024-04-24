our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

intersect = our_routes.intersection(competitor_routes)
print(intersect)

diff_route = our_routes.difference(competitor_routes)
print(diff_route)

sym_route = our_routes.symmetric_difference(competitor_routes)
print(sym_route)