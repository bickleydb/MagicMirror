import * as $ from 'jquery'

export interface InterpolatorFunction {
    (previousState : number) : number
}

export interface Interpolator {
    GetValue : InterpolatorFunction
}

export class LinearInterpolator  {

}

export interface Animation {
    
}

export interface AnimationConfig {
    duration : number,
    easing : string,
    complete : Function,
}

export class LinearAnimation implements Animation{

    private animatedElement : HTMLElement;

    constructor(animatingElement : HTMLElement) {
        this.animatedElement = animatingElement;
    }

    Start() : void {
        $(this.animatedElement).animate({

        });
    }

}