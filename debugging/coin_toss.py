from logging import debug, DEBUG, disable, basicConfig, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

if __name__ == '__main__':
    main()