/*
 * Copyright (C) 2018 René Dudfield. GPLv3 License.
 *
 * hey,
 *
 *   this is a demonstration of the fundamental concepts you need
 *   for a SDL2 app written in C. In other words, the basics.
 *
 *   When you compile and run the app, it shows you about these
 *   concepts too. There's a bunch of links for more details.
 *
 *   Happy hacking!
 *
 * René Dudfield,
 *
 *
 * Fundamental basic SDL2 knowledge.
 *   - creating windows
 *   - coordinate system
 *   - error handling
 *   - color and pixel formats
 *   - surfaces
 *   - rects
 *   - event handling for keyboard
 *
 *
 * https://wiki.libsdl.org/Installation
 *   Debian/Ubuntu
 *     sudo yum install SDL2-devel
 *   Fedora/Redhat
 *     sudo yum install SDL2-devel
 *   Mac OSX
 *     brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf
 *
 * Compiling
 *   gcc -o hey hey.c `sdl2-config --cflags --libs`
 *   ./hey
 *
 *
 * Color: red, green, blue, alpha.
 * Rect:  x, y, width, height. Top left is (0, 0).
 * Time:  1000 miliseconds in a second.
 *
 * All SDL functions and structures start with a 'SDL_' prefix.
 *
 *
 *
 * Functions and structures.
 *
 * SDL_Init, call this first to start using SDL.
 *   https://wiki.libsdl.org/SDL_Init
 *
 *   int SDL_Init(Uint32 flags)
 *
 * SDL_GetError, last error that occured as a string.
 *   https://wiki.libsdl.org/SDL_GetError
 *
 *   const char* SDL_GetError(void)
 *
 * SDL_CreateWindow, open a window.
 *   https://wiki.libsdl.org/SDL_CreateWindow
 *   https://wiki.libsdl.org/SDL_WindowFlags
 *
 *   Flags are window properties, like FULL_SCREEN.
 *   SDL_Window* SDL_CreateWindow(const char* title,
 *                                int         x,
 *                                int         y,
 *                                int         w,
 *                                int         h,
 *                                Uint32      flags)
 *
 * SDL_PollEvent, ask for currently available events (keyboard etc).
 *   https://wiki.libsdl.org/SDL_PollEvent
 *   https://wiki.libsdl.org/CategoryKeyboard
 *   https://wiki.libsdl.org/CategoryMouse
 *
 *   int SDL_PollEvent(SDL_Event* event)
 *
 * SDL_Surface, pixels used in drawing with software renderers.
 *   https://wiki.libsdl.org/SDL_Surface
 *
 * SDL_GetWindowSurface, gets SDL_Surface associated with a SDL_Window.
 *   https://wiki.libsdl.org/SDL_GetWindowSurface
 *
 *   SDL_Surface* SDL_GetWindowSurface(SDL_Window* window)
 *
 * SDL_PixelFormat, pixel structure with info like bits per color.
 *   https://wiki.libsdl.org/SDL_PixelFormat
 *
 * SDL_MapRGB, for a R,G,B color it gives closest color in SDL_PixelFormat.
 *   https://wiki.libsdl.org/SDL_MapRGB
 *
 *   Uint32 SDL_MapRGB(const SDL_PixelFormat* format,
 *                     Uint8                  r,
 *                     Uint8                  g,
 *                     Uint8                  b)
 *
 * SDL_Rect, rectangle structure, top left is origin at 0,0.
 *   https://wiki.libsdl.org/SDL_Rect
 *
 * SDL_FillRect, fast fill of rectangle with color.
 *   https://wiki.libsdl.org/SDL_FillRect
 *
 *   int SDL_FillRect(SDL_Surface*    dst,
 *                    const SDL_Rect* rect,
 *                    Uint32          color)
 *
 * SDL_UpdateWindowSurface, copy window surface to the screen.
 *   https://wiki.libsdl.org/SDL_UpdateWindowSurface
 *
 *   int SDL_UpdateWindowSurface(SDL_Window* window)
 *
 * SDL_Delay, wait milliseconds.
 *   https://wiki.libsdl.org/SDL_Delay
 *
 *   void SDL_Delay(Uint32 ms)
 *
 * SDL_DestroyWindow, close and clean up window when you are done.
 *   https://wiki.libsdl.org/SDL_DestroyWindow
 *
 *   void SDL_DestroyWindow(SDL_Window* window)
 *
 * SDL_Quit, clean up, and quit all SDL systems.
 *   https://wiki.libsdl.org/SDL_Quit
 *
 */
#include <SDL.h>
#include <stdio.h>

const int WINDOW_WIDTH = 640;
const int WINDOW_HEIGHT = 480;

int main(int argc, char* args[]) {
  SDL_Window* window = NULL;
  SDL_Surface* windowSurface = NULL;
  SDL_Event e;
  char windowTitle[ 128 ] ;

  if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    fprintf(stderr, "SDL_Init SDL_GetError: %s\n", SDL_GetError());
    goto finish;
  }


  window = SDL_CreateWindow("hey",
    SDL_WINDOWPOS_UNDEFINED,
    SDL_WINDOWPOS_UNDEFINED,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    SDL_WINDOW_RESIZABLE
  );
  if (window == NULL) {
    fprintf(stderr, "SDL_CreateWindow SDL_GetError: %s\n", SDL_GetError());
    goto finish;
  }

  windowSurface = SDL_GetWindowSurface(window);

  Uint32 redColorInSurfaceFormat = SDL_MapRGB(windowSurface->format,
    0xFF, // red,    255 == 0xFF
    0x0,  // green,  0   == 0x0
    0x0   // blue,   0   == 0x0
  );
  Uint32 greenColorInSurfaceFormat = SDL_MapRGB(
    windowSurface->format,
    0x0,  // red
    0xFF, // green
    0x0   // blue
  );
  Uint32 blueColorInSurfaceFormat = SDL_MapRGB(
    windowSurface->format,
    0x0,  // red
    0x0,  // green
    0xFF  // blue
  );



  SDL_Rect rectAreaToFill = { 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT };
  rectAreaToFill.x = 0;
  rectAreaToFill.y = 0;
  rectAreaToFill.w = WINDOW_WIDTH;
  rectAreaToFill.h = WINDOW_HEIGHT;

  SDL_FillRect(
       windowSurface,
       &rectAreaToFill,
    redColorInSurfaceFormat
  );


  sprintf(windowTitle,
          "Hey."
          " screen(640x480) fill rect(x%d,y:%d,w:%d,h:%d)"
          " with red(0xFF,0x00,0x0). Sleep 4000ms.",
          rectAreaToFill.x,
          rectAreaToFill.y,
          rectAreaToFill.w,
          rectAreaToFill.h);


  SDL_SetWindowTitle(window, windowTitle);
  while(SDL_PollEvent(&e) != 0) {}

  SDL_UpdateWindowSurface(window);

  int milisecondsToWait = 1000;
  int seconds = 4;
  SDL_Delay(milisecondsToWait * seconds);




  // x == 0 is far left of window
  // y == 0 is top of window
  rectAreaToFill.x = WINDOW_WIDTH / 3;
  rectAreaToFill.y = WINDOW_HEIGHT / 3;
  SDL_FillRect(
         windowSurface,
         &rectAreaToFill,
    greenColorInSurfaceFormat
  );

  sprintf(windowTitle,
          " fill rect(x%d,y:%d,w:%d,h:%d)"
          " with green(0x0,0xFF,0x0). Sleep 4000ms.",
          rectAreaToFill.x,
          rectAreaToFill.y,
          rectAreaToFill.w,
          rectAreaToFill.h);
  SDL_SetWindowTitle(window, windowTitle);
  while(SDL_PollEvent(&e) != 0) {}

  SDL_UpdateWindowSurface(window);
  seconds = 4;
  SDL_Delay(1000 * seconds);



  // x == WINDOW_WIDTH is far right of window.
  // y == WINDOW_WIDTH is bottom right of window.
  rectAreaToFill.x = (WINDOW_WIDTH / 3) * 2;
  rectAreaToFill.y = (WINDOW_HEIGHT / 3) * 2;
  SDL_FillRect(
        windowSurface,
        &rectAreaToFill,
    blueColorInSurfaceFormat
  );
  sprintf(windowTitle,
          " Filling rect(x%d,y:%d,w:%d,h:%d)"
          " with blue(0x0,0x00,0xFF). Sleep 4000ms.",
          rectAreaToFill.x,
          rectAreaToFill.y,
          rectAreaToFill.w,
          rectAreaToFill.h);
  SDL_SetWindowTitle(window, windowTitle);
  while(SDL_PollEvent(&e) != 0) {}

  SDL_UpdateWindowSurface(window);
  seconds = 4;
  SDL_Delay(1000 * seconds);


  sprintf(windowTitle, "Waiting for SDLK_q or SDLK_ESCAPE key to quit.");
  SDL_SetWindowTitle(window, windowTitle);

  int going = 1;
  while (going) {
    while(SDL_PollEvent(&e) != 0) {
      if(e.type == SDL_QUIT) {
        going = 0;
      }
      if(e.type == SDL_KEYDOWN) {
        switch( e.key.keysym.sym ) {
          case SDLK_ESCAPE: going = 0; break;
          case SDLK_q: going = 0; break;
        }
      }
    }
  }


finish:
  if(window) SDL_DestroyWindow(window);
  SDL_Quit();
  return 0;
}