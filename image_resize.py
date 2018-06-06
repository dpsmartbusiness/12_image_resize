import argparse
from PIL import Image
from os.path import splitext, abspath, basename, split


def create_parser():
    parser = argparse.ArgumentParser(
        description='Image resizer'
    )
    parser.add_argument(
        '-fp',
        '--filepath',
        help='Image that user want to change'
    )
    parser.add_argument(
        '-s',
        '--scale',
        type=int,
        default=1,
        help='Scale multiplier'
    )
    parser.add_argument(
        '-w',
        '--width',
        type=int,
        default=None,
        help='New image width'
    )
    parser.add_argument(
        '-he',
        '--height',
        type=int,
        default=None,
        help='New image height'
    )
    parser.add_argument(
        '--savepath',
        '-sp',
        default=None,
        help='Path to save resized image'
    )
    return parser


def open_image(source_image):
    try:
        image = Image.open(source_image)
        return image
    except IOError:
        return None


def get_new_size(source_image, new_width, new_height, scale):
    width, height = source_image.size
    size_format = width/height
    if new_width and new_height:
        return new_width, new_height
    elif new_width:
        return round(new_width / size_format), new_width
    elif new_height:
        return round(new_height * size_format), new_height
    else:
        return round(width * scale), round(height * scale)


def resize_image(image, new_size):
    return image.resize(new_size)


def get_savepath(resized_image, source_image, path_to_save):
    image_name, image_ext = splitext(source_image.filename)
    width, height = resized_image.size
    save_template = '{}__{}x{}{}'.format(
        image_name,
        width, height,
        image_ext
    )
    if path_to_save:
        savepath = path_to_save + '/' + save_template
        print(savepath)
    else:
        savepath = save_template
    return savepath


def save_image(image, savepath):
    return image.save(savepath)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    scale = args.scale
    if scale != 1 and (args.width or args.height):
        print('Pls enter only scale or image sizes')
    else:
        try:
            source_image = open_image(args.filepath)
            new_size = get_new_size(
                source_image,
                args.width,
                args.height,
                args.scale)
            resized_image = resize_image(source_image, (new_size))
            savepath = get_savepath(resized_image, source_image, args.savepath)
            path, file = split(abspath(savepath))
            try:
                saved_image = save_image(resized_image, savepath)
                print('Image {} was succesfully resized and save to {}'.format(
                    basename(savepath),
                    path
                ))
            except PermissionError:
                print('Permission Error. Change savepath and try again')
        except AttributeError:
            print('Filepath not found pls. Try again...')