from pydub import AudioSegment, silence
audio = AudioSegment.from_mp3('/Users/jojo/Documents/编程/英语新素养k段-绘本demo/assets/sound/嘉岚3.0-2026-05-25-19-17-I-want-a-party.-I-want-some-cards.-I-want-some-g.mp3')
# Try different thresholds
for thresh in [-25, -30, -35, -40]:
    for min_sil in [150, 200, 250, 300]:
        intervals = silence.detect_silence(audio, min_silence_len=min_sil, silence_thresh=thresh)
        speech = []
        prev = 0
        for s in intervals:
            if s[0] > prev:
                speech.append((prev, s[0]))
            prev = s[1]
        if prev < len(audio):
            speech.append((prev, len(audio)))
        if len(speech) >= 7 and len(speech) <= 10:
            print(f"thresh={thresh} min_sil={min_sil} => {len(speech)} segments:")
            for i, seg in enumerate(speech):
                print(f"  {i+1}: {seg[0]/1000:.3f}s - {seg[1]/1000:.3f}s ({(seg[1]-seg[0])/1000:.3f}s)")
            print()