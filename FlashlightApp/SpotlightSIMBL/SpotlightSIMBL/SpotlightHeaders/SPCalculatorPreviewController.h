//
//     Generated by class-dump 3.5 (64 bit).
//
//     class-dump is Copyright (C) 1997-1998, 2000-2001, 2004-2013 by Steve Nygard.
//

#import "SPPreviewController.h"

@class NSArray, NSNumberFormatter, NSTextField, NSView, SPLineView;

@interface SPCalculatorPreviewController : SPPreviewController
{
    NSTextField *_interpretedText;
    NSTextField *_currencyUpdated;
    SPLineView *_line;
    NSView *_spacer1;
    NSView *_spacer2;
    NSNumberFormatter *_formatter;
    NSArray *_slices;
}

+ (id)sharedPreviewController;
@property(retain) NSArray *slices; // @synthesize slices=_slices;
@property __weak NSNumberFormatter *formatter; // @synthesize formatter=_formatter;
@property __weak NSView *spacer2; // @synthesize spacer2=_spacer2;
@property __weak NSView *spacer1; // @synthesize spacer1=_spacer1;
@property __weak SPLineView *line; // @synthesize line=_line;
@property __weak NSTextField *currencyUpdated; // @synthesize currencyUpdated=_currencyUpdated;
@property __weak NSTextField *interpretedText; // @synthesize interpretedText=_interpretedText;
- (void).cxx_destruct;
- (void)setRepresentedObject:(id)arg1;
- (void)awakeFromNib;
- (void)setupForObject:(id)arg1;
- (id)init;

@end

