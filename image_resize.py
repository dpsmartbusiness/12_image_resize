import argparse
from PIL import Image
from os.path import splitext, abspath, basename, split, join


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
        type=float,
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
        help='Directory name to save resized image (for example: c:/devman)'
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
        savepath = join(path_to_save, save_template)
    else:
        savepath = save_template
    return savepath


def save_image(image, savepath):
    return image.save(savepath)


def get_notice(width, height, savepath):
    if savepath is None:
        print('File save to source directory!')
    elif width and height:
        print('Your are change width and height!!!(bad for proportions)')


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    try:
        if args.filepath is None:
            exit('You forget to specify source image name or filepath')
        elif args.scale == 1 and not (args.width or args.height):
            exit('Pls enter arguments for resizing')
        elif args.scale != 1 and (args.width or args.height):
            exit('Pls enter only scale or image sizes')
        source_image = open_image(args.filepath)
        new_size = get_new_size(source_image, args.width, args.height, args.scale)
        resized_image = resize_image(source_image, (new_size))
        savepath = get_savepath(resized_image, source_image, args.savepath)
        path, filename = split(abspath(savepath))
        saved_image = save_image(resized_image, savepath)
        get_notice(args.width, args.height, args.savepath)
        print('Image {} was succesfully resized and save to {}'.format(
            basename(savepath),
            path
            ))
    except AttributeError:
        print('Filepath not found. Pls Try again...')
    except (PermissionError, OSError):
        print('Permission Error. Change savepath and try again')
    except ValueError:
        print('Scale, height and width must be more than 0. Try again...')