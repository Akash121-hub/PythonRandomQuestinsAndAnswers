desired = {
  "dialog_transparency": "disabled",
  "home_realm_id": "ld5"  
}
    
current = {
    "dialog_transparency": "disabled",
    "home-realm-id": "ny1"    
}

# print(desired.items())
for i,j in current.items():
  if i not in desired.items():
    desired[i] = j

print(desired)

