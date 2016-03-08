import os
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from scipy.io import wavfile


def load_dataset(topleveldir):
    target_names = []
    dataset = []
    for path, dirs, files in os.walk(topleveldir):
        for f in files:
            if not f.endswith('.wav'):
                logger.debug('skipping non .wav: %s' % f)
                continue
            wav_file = os.path.join(path, f)
            tail, track = os.path.split(wav_file)
            tail, dir1 = os.path.split(tail)
            target_names.append(dir1)  # feature targets
            logger.info('adding file: %s with target: %s' % (wav_file, dir1))
            samplerate, wavedata = wavfile.read(wav_file)
            dataset.append({'data': wavedata, 'target': dir1, 'samplerate': samplerate, 'filename': wav_file})
    return dataset
