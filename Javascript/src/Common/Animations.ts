
export type InterpolatorFunction = (previousState: number)  => number;

// tslint:disable-next-line: interface-name
export interface Interpolator {
    GetValue: InterpolatorFunction;
}

export class LinearInterpolator  {

}

// tslint:disable-next-line: interface-name
export interface AnimationConfig {
    duration: number;
    easing: string;
    // tslint:disable-next-line: ban-types
    complete: Function;
}
