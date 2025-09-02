if animal_detected and not siren_playing:
    print("🔴 Animal detected → Siren ON")
    siren.play(-1)
    siren_playing = True
elif not animal_detected and siren_playing:
    print("🟢 Animal gone → Siren OFF")
    siren.stop()
    siren_playing = False
