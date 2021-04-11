def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
  print("Attempt " + str(n) + " failed")
b=s.count()


retry(create_user, 3)
retry(stop_service, 5)

